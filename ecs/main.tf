provider "aws" {
	region = "us-east-1"
}

resource "aws_security_group" "ecs-securitygroup" {
  vpc_id = "${var.vpc_id}"
  name = "ecs"
  description = "security group for ecs"
  egress {
      from_port = 0
      to_port = 0
      protocol = "-1"
      cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
      from_port = 22
      to_port = 22
      protocol = "tcp"
      cidr_blocks = ["${var.sg_cidr_block}"]
  }
  ingress {
      from_port = 80
      to_port = 80
      protocol = "tcp"
      cidr_blocks = ["${var.sg_cidr_block}", "0.0.0.0/0"]
  }
    ingress {
      from_port = 8081
      to_port = 8081
      protocol = "tcp"
      cidr_blocks = ["${var.sg_cidr_block}", "0.0.0.0/0"]
  }

  tags {
    Name = "ecs"
  }
}

resource "aws_launch_configuration" "ecs-launchconfig" {
  name_prefix          = "ecs-launchconfig"
  image_id             = "${var.ecs_ami}"
  instance_type        = "${var.ecs_instance_type}"
  key_name             = "${var.ecs_key_name}"
  iam_instance_profile = "${var.iam_role}"
  security_groups      = ["${aws_security_group.ecs-securitygroup.id}"]
  user_data            = "#!/bin/bash\necho 'ECS_CLUSTER=${var.ecs_cluster_name}' >> /etc/ecs/ecs.config"
  lifecycle              { create_before_destroy = true }
  depends_on = ["aws_ecs_cluster.main"]
}


resource "aws_autoscaling_attachment" "asg_attachment_group" {
  autoscaling_group_name = "${aws_autoscaling_group.ecs-autoscaling.id}"
  elb                    = "${aws_elb.ecs-elb.id}"
  depends_on = ["aws_elb.ecs-elb"]
 }

#load balancer
resource "aws_elb" "ecs-elb" {
  name = "ecs-elb"

  listener {
    instance_port = 8080
    instance_protocol = "http"
    lb_port = 80
    lb_protocol = "http"
  }

  health_check {
    healthy_threshold = 3
    unhealthy_threshold = 3
    timeout = 30
    target = "HTTP:8080/health"
    interval = 60
  }

  cross_zone_load_balancing = true
  idle_timeout = 400
  connection_draining = true
  connection_draining_timeout = 400
  subnets = ["${var.aws_subnet}"]
  security_groups = ["${aws_security_group.ecs-securitygroup.id}"]

  tags {
    Name = "ecs-elb"
  }
}


resource "aws_ecs_cluster" "main" {
    name = "${var.ecs_cluster_name}"
}


resource "aws_autoscaling_group" "ecs-autoscaling" {
  name                 = "ecs-autoscaling"
  vpc_zone_identifier  = [ "${var.aws_subnet}" ]
  launch_configuration = "${aws_launch_configuration.ecs-launchconfig.name}"
  min_size             = 1
  max_size             = 1
  tag {
      key = "Application"
      value = "ecs-ec2-container"
      propagate_at_launch = true
  }
  tag {
    key                 = "CreatorName"
    value               = "${var.tag_creator_name}"
    propagate_at_launch = true
    }
  tag {
    key                 = "Department"
    value               = "${var.tag_department}"
    propagate_at_launch = true
    }
  tag {
    key                 = "Environment"
    value               = "${var.tag_environment}"
    propagate_at_launch = true
    }
  tag {
    key                 = "Name"
    value               = "${var.tag_name}"
    propagate_at_launch = true
    }
  tag {
    key                 = "TeamName"
    value               = "${var.tag_team_name}"
    propagate_at_launch = true
    }
}


resource "aws_ecs_task_definition" "service" {
  family                = "service"
  container_definitions = "${file("task-definitions/service.json")}"
}

resource "aws_api_gateway_rest_api" "ecs_hydra_core" {
  name        = "ecs_hydra_core"
  description = "ECS Hydra Core"
}

resource "aws_api_gateway_resource" "resource_health" {
  rest_api_id = "${aws_api_gateway_rest_api.ecs_hydra_core.id}"
  parent_id   = "${aws_api_gateway_rest_api.ecs_hydra_core.root_resource_id}"
  path_part   = "health"
}

resource "aws_api_gateway_method" "method_health" {
  rest_api_id   = "${aws_api_gateway_rest_api.ecs_hydra_core.id}"
  resource_id   = "${aws_api_gateway_resource.resource_health.id}"
  http_method   = "GET"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "integration_health" {
  rest_api_id = "${aws_api_gateway_rest_api.ecs_hydra_core.id}"
  resource_id = "${aws_api_gateway_resource.resource_health.id}"
  http_method = "${aws_api_gateway_method.method_health.http_method}"
  uri = "http://hydra-core.awsedsgpnp.com/health"
  type                        = "HTTP_PROXY"
  integration_http_method     = "GET"
}


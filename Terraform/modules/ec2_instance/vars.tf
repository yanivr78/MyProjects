variable "AWS_REGION" {
  default = "us-east-1"
}

variable "PATH_TO_PRIVATE_KEY" {
  default = "mykey"
}

variable "JENKINS_SG" {
  default = "jenkins_allow_ssh"
}

variable "VPC_ID" {
  default = "vpc-00000000example"
}

variable "VPC_CIDR_BLOCK" {
  default = "10.0.0.0/22"
}

variable "SUBNET_ID" {
  default = "subnet-00000000example"
}

variable "PATH_TO_PUBLIC_KEY" {
  default = "~/.ssh/id_rsa.pub"
}

variable "PATH_TO_LOCAL_KEY" {
  default = "~/.ssh/id_rsa"
}

variable "AMIS" {
  type = "map"
  default = {
    us-east-1 = "ami-13be557e"
    us-west-2 = "ami-06b94666"
    eu-west-1 = "ami-844e0bf7"
  }
}

variable "INSTANCE_USERNAME" {
  default = "ubuntu"
}

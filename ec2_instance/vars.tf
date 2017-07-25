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
	default = "vpc-b3bd0ad5"
}

variable "VPC_CIDR_BLOCK" {
	default = "10.230.36.0/22"
}

variable "SUBNET_ID" {
        default = "subnet-d4c8a3f9"
}

variable "PATH_TO_PUBLIC_KEY" {
	default = "/home/centos/.ssh/id_rsa.pub"
}

variable "PATH_TO_LOCAL_KEY" {
        default = "/home/centos/.ssh/id_rsa"
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



provider "aws" {
    region = "${var.AWS_REGION}"
}

resource "aws_security_group" "allow_ssh" {
  name        = "jenkins_allow_ssh"
  description = "Allow ssh inbound traffic"
  vpc_id = "${var.VPC_ID}"

 ingress {
    from_port   = 0
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["${var.VPC_CIDR_BLOCK}"]
  }

}
resource "aws_key_pair" "mykeypair" {
  key_name = "mykeypair"
  public_key = "${file("${var.PATH_TO_PUBLIC_KEY}")}"
}

resource "aws_instance" "jenkins_sample" {
  ami           = "${lookup(var.AMIS, var.AWS_REGION)}"
  instance_type = "t2.micro"
  vpc_security_group_ids = ["${aws_security_group.allow_ssh.id}"]
  key_name = "${aws_key_pair.mykeypair.key_name}"
  subnet_id = "${var.SUBNET_ID}"
    tags {
    Name = "Jenkins_Sample"
  }  

provisioner "file" {
  source      = "script.sh"
  destination = "/tmp/setup.sh"
}

provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/setup.sh",
      "sudo /tmp/setup.sh"
    ]
  }

  connection {
    user = "${var.INSTANCE_USERNAME}"
    private_key = "${file("${var.PATH_TO_LOCAL_KEY}")}"
  }
  


}


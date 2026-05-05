provider "aws" {
  region = "eu-north-1"
}

# Generate RSA key
resource "tls_private_key" "example" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# Register public key in AWS
resource "aws_key_pair" "example" {
  key_name   = "terraform-key"
  public_key = tls_private_key.example.public_key_openssh
}

# Security Group - Allow SSH
resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"

  ingress {
    description = "SSH from anywhere"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 instance with key and security group attached
resource "aws_instance" "example" {
  ami                    = "ami-075449515af5df0d1"
  instance_type          = "t3.micro"
  key_name               = aws_key_pair.example.key_name
  vpc_security_group_ids = [aws_security_group.allow_ssh.id]

  tags = {
    Name = "Terraform-Example"
  }
}

# Outputs
output "instance_public_ip" {
  value = aws_instance.example.public_ip
}

output "private_key" {
  value     = tls_private_key.example.private_key_pem
  sensitive = true
}
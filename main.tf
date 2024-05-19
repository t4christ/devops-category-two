# VPC
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

# Subnet
resource "aws_subnet" "main" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
}

# Security Group
resource "aws_security_group" "instance" {
  name        = "instance_security_group"
  description = "Allow SSH and HTTP"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
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

# Keypair creation ggb
resource "aws_key_pair" "deployer"{
    key_name   = "deployer-key"
    public_key = file("/Users/dibaalakari/.ssh/id_rsa.pub")
}


# EC2 Instance
resource "aws_instance" "web" {
  ami           = "ami-0bb84b8ffd87024d8"  # Amazon Linux 2 AMI
  instance_type = var.instance_type
  key_name      = aws_key_pair.deployer.key_name
  subnet_id     = aws_subnet.main.id
  vpc_security_group_ids = [aws_security_group.instance.id]

  root_block_device {
    volume_size = 8  # Size in GB
  }

  ebs_block_device {
    device_name = "/dev/sdh"
    volume_size = 20  # Size in GB
  }

  ebs_block_device {
    device_name = "/dev/sdi"
    volume_size = 20  # Size in GB
  }

  tags = {
    Name = "WebServerInstance"
  }
}

# DynamoDB Table
resource "aws_dynamodb_table" "basic_dynamodb_table" {
  name           = "BasicDynamoDBTable"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "Id"

  attribute {
    name = "Id"
    type = "S"
  }
}
# Random Password
resource "random_password" "password" {
    length = 8
    special = true
    keepers = {
        username = var.db_user
    }
}
# RDS PostgreSQL
resource "aws_db_instance" "postgres" {
  allocated_storage    = var.db_allocated_storage
  engine               = "postgres"
  engine_version       = "16.2"
  instance_class       = var.db_instance_class
  identifier                 = var.db_name
  username             = var.db_user
#   password             = var.db_password
  password             = random_password.password.result
#   parameter_group_name = "default.postgres12"
  skip_final_snapshot  = true
  vpc_security_group_ids = [aws_security_group.instance.id]
  db_subnet_group_name = aws_db_subnet_group.main.name
}

# resource "aws_subnet" "main" {
#   vpc_id     = aws_vpc.main.id
#   cidr_block = "10.0.1.0/24"
#   availability_zone = "us-east-1a"
# }

resource "aws_subnet" "secondary" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.2.0/24"
  availability_zone = "us-east-1b"
}

resource "aws_db_subnet_group" "main" {
  name       = "main"
  subnet_ids = [aws_subnet.main.id, aws_subnet.secondary.id]

  tags = {
    Name = "MainDBSubnetGroup"
  }
}
# resource "aws_db_subnet_group" "main" {
#   name       = "main"
#   subnet_ids = [aws_subnet.main.id]

#   tags = {
#     Name = "MainDBSubnetGroup"
#   }
# }

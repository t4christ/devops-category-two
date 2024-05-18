variable "aws_region" {
  description = "The AWS region to deploy in"
  default     = "us-east-1"
}


variable "instance_type" {
  description = "The instance type to use"
  default     = "t2.micro"
}

variable "key_name" {
  description = "The name of the key pair to use"
  default     = "key_name"
}

variable "public_key_path" {
  description = "Path to the public key to use"
}

variable "db_name" {
  description = "The name of the PostgreSQL database"
  default     = "mydb"
}

variable "db_user" {
  description = "The username for the PostgreSQL database"
  default     = "postgres"
}

variable "db_password" {
  description = "The password for the PostgreSQL database"
}

variable "db_instance_class" {
  description = "The instance class for RDS"
  default     = "db.t3.micro"
}

variable "db_allocated_storage" {
  description = "The allocated storage for RDS in GB"
  default     = 20
}

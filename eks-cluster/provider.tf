data "aws_caller_identity" "current" {}

provider "aws" {
  region  = "us-east-1"
  profile = "terraform-ctwo"
}
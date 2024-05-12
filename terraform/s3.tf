resource "aws_s3_bucket" "ctwo" {
  bucket = "ctwo-bucket"

  tags = {
    Name        = "ctwo-bucket"
    Environment = "Dev"
  }
}
resource "aws_s3_bucket" "ctwo" {
  bucket = "devopstwo-bucket"

  tags = {
    Name        = "devopstwo-bucket"
    Environment = "Dev"
  }
}

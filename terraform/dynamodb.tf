resource "aws_dynamodb_table" "dynamodb-cone-state-lock" {
  name           = "devopstwo"
  hash_key       = "LockID"
  read_capacity  = 20
  write_capacity = 20

  attribute {
    name = "LockID"
    type = "S"
  }
}

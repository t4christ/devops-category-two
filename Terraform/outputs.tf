output "instance_id" {
  value = aws_instance.web.id
}

output "instance_public_ip" {
  value = aws_instance.web.public_ip
}

output "instance_public_dns" {
  value = aws_instance.web.public_dns
}

output "dynamodb_table_name" {
  value = aws_dynamodb_table.basic_dynamodb_table.name
}

output "rds_endpoint" {
  value = aws_db_instance.postgres.endpoint
}

output "db_password" {
  value     = random_password.password.result
  sensitive = true
}
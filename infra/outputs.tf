output "master_public_ip" {
  description = "Master Node Public IP"
  value       = aws_instance.master.public_ip
}

output "worker1_public_ip" {
  description = "Worker 1 Node Public IP"
  value       = aws_instance.worker1.public_ip
}

output "worker2_public_ip" {
  description = "Worker 2 Node Public IP"
  value       = aws_instance.worker2.public_ip
}

output "rds_endpoint" {
  description = "Postgres RDS Endpoint Adresi"
  value       = aws_db_instance.postgres.endpoint
}

output "rds_password" {
  description = "Postgres RDS Sifresi"
  value       = random_password.db_password.result
  sensitive   = true # Ekrana acik sekilde basicak kadar acemi degiliz :)
}
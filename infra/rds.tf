# Rastgele ve guvenli veritabani sifresi olusturucu
resource "random_password" "db_password" {
  length  = 16
  special = false
}

# RDS Postgres Instance
resource "aws_db_instance" "postgres" {
  identifier           = "${var.project_name}-db"
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "16.3" 
  instance_class       = "db.t3.micro"
  username             = "appuser"
  password             = random_password.db_password.result
  
  vpc_security_group_ids = [aws_security_group.capstone_sg.id]
  
  publicly_accessible    = false # Disaridan erisim YOK (Best Practice)
  skip_final_snapshot    = true  # Kapatirken ugrasmasin, direkt silsin

  tags = {
    Name    = "${var.project_name}-db"
    Owner   = var.owner
    Project = var.project_name
  }
}
# Master Node (k3s Server)
resource "aws_instance" "master" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.small"
  vpc_security_group_ids = [aws_security_group.capstone_sg.id]
  key_name               = var.key_name

  tags = {
    Name    = "${var.project_name}-master"
    Owner   = var.owner
    Project = var.project_name
    Role    = "k3s-master"
  }
}

# Worker Node 1 (k3s Agent)
resource "aws_instance" "worker1" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.small"
  vpc_security_group_ids = [aws_security_group.capstone_sg.id]
  key_name               = var.key_name

  tags = {
    Name    = "${var.project_name}-worker-1"
    Owner   = var.owner
    Project = var.project_name
    Role    = "k3s-worker"
  }
}

# Worker Node 2 (k3s Agent)
resource "aws_instance" "worker2" {
  ami                    = data.aws_ami.ubuntu.id
  instance_type          = "t3.small"
  vpc_security_group_ids = [aws_security_group.capstone_sg.id]
  key_name               = var.key_name

  tags = {
    Name    = "${var.project_name}-worker-2"
    Owner   = var.owner
    Project = var.project_name
    Role    = "k3s-worker"
  }
}
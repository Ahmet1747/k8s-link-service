terraform {
  backend "s3" {
    bucket         = "capstone-tfstate-ahmetcan" 
    key            = "terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
  }
}
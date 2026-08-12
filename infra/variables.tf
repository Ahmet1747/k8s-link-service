variable "aws_region" {
  description = "AWS Bölgesi"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Proje Adı"
  type        = string
  default     = "capstone"
}

variable "owner" {
  description = "Sorumlu/Sahip"
  type        = string
  default     = "ahmetcan" 
}

variable "my_ip" {
  description = "Senin Public IP Adresin (SSH erisimi icin)"
  type        = string
 default     = "***********/32" 
 }

variable "key_name" {
  description = "AWS SSH Key Pair Adi"
  type        = string
  default     = "staj-ahmetcan" 
}
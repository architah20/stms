variable "region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "key_name" {
  description = "Name of an existing EC2 key pair (for SSH)"
  type        = string
}

variable "dockerhub_username" {
  description = "Your Docker Hub username (image: <username>/stms:latest)"
  type        = string
}

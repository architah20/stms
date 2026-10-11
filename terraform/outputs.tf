output "public_ip" {
  value = aws_instance.stms.public_ip
}

output "app_url" {
  value = "http://${aws_instance.stms.public_ip}:5000"
}

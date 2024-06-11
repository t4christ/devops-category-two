#resource "aws_instance" "web" {
#  ami               = data.aws_ami.ubuntu.id
#  instance_type     = "t3.micro"
#  availability_zone = "us-east-1a"

#  tags = {
#    Name        = "ctwoec2"
#    Environment = "Dev"
#  }
#}

#resource "aws_volume_attachment" "ebs_att" {
#  device_name = "/dev/sdh"
#  volume_id   = aws_ebs_volume.ctwo.id
#  instance_id = aws_instance.web.id
#}

#resource "aws_ebs_volume" "ctwo" {
#  availability_zone = "us-east-1a"
#  size              = 40

#  tags = {
#    Name        = "ctwoebs"
#    Environment = "Dev"
#  }
#}

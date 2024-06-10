data "aws_ssm_parameter" "eks-ami-18" {
  name = "/aws/service/eks/optimized-ami/1.30/amazon-linux-2/recommended/image_id"
  # depends_on = [ aws_iam_policy.eks_policy , aws_iam_user_policy_attachment.eks_user_policy_attachment]
}

resource "aws_launch_template" "launch_template" {
  depends_on = [aws_key_pair.workernode_key_pair]
  name       = "${local.env}-${local.project}-eks-worker-lt"
  iam_instance_profile {
    arn = aws_iam_instance_profile.eks-worker-iamrole-instances-profile.arn
  }
  block_device_mappings {
    device_name = "/dev/xvda"
    ebs {
      volume_size = 100
      volume_type = "gp3"
      throughput  = 125
      iops        = 3000
    }
  }
  image_id                             = data.aws_ssm_parameter.eks-ami-18.value
  instance_initiated_shutdown_behavior = "terminate"
  instance_type                        = local.eks_worker_node_instance_type
  key_name                             = aws_key_pair.workernode_key_pair.key_name
  vpc_security_group_ids               = [aws_security_group.eks-cluster-sg.id]
  user_data                            = base64encode(local.eks_worker_node_userdata)
  tags = merge(
    tomap({ "Name" = "${local.env}-${local.project}-launch-template" }),
    tomap({ "ResourceType" = "LAUNCHTEMPLATE" }),
  local.common_tags)

  tag_specifications {
    resource_type = "instance"
    tags = merge(
      tomap({ "Name" = "${local.env}-${local.project}-eks-worker-node" }),
      tomap({ "ResourceType" = "EC2" }),
      local.common_tags,
      tomap({ "k8s.io/cluster-autoscaler/${local.env}-${local.project}-eks-cluster" = "owned" }),
    tomap({ "kubernetes.io/cluster/${local.env}-${local.project}-eks-cluster" = "owned" }))
  }

  tag_specifications {
    resource_type = "volume"
    tags = merge(
      tomap({ "Name" = "${local.env}-${local.project}-eks-worker-node-volume" }),
      tomap({ "ResourceType" = "EBS" }),
    local.common_tags)
  }
  //  lifecycle {
  //    prevent_destroy = true
  //  }
}

resource "aws_key_pair" "workernode_key_pair" {
  key_name   = "${local.env}-${local.project}-eks-worker-node-keypair"
  public_key = local.eks_worker_node_keypair

  tags = merge(
    tomap({ "Name" = "${local.env}-${local.project}-eks-worker-node-keypair" }),
  local.common_tags)
  //  lifecycle {
  //    prevent_destroy = true
  //  }
}
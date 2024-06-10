resource "aws_eks_cluster" "eks" {
  name = local.eks_cluster_name

  vpc_config {
    subnet_ids              = [aws_subnet.private-subnet-1a.id, aws_subnet.private-subnet-1b.id, aws_subnet.private-subnet-1c.id]
    security_group_ids      = [aws_security_group.eks-cluster-sg.id]
    endpoint_private_access = false
    endpoint_public_access  = true
  }

  access_config {
    authentication_mode                         = "API_AND_CONFIG_MAP"
    bootstrap_cluster_creator_admin_permissions = true
  }

  enabled_cluster_log_types = ["api", "audit"]
  role_arn                  = aws_iam_role.eks-cluster-role.arn
  version                   = local.k8_version
  tags = merge(
    tomap({ "Name" = join("-", [local.env, local.project, "eks-cluster"]) }),
    tomap({ "ResourceType" = "EKS" }),
  local.common_tags)

  # depends_on = [ aws_iam_policy.eks_policy, aws_iam_user_policy_attachment.eks_user_policy_attachment ]
}
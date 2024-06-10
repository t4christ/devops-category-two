# IAM Policy for EKS Cluster Management
# resource "aws_iam_policy" "eks_policy" {
#   name        = "EKSPolicy"
#   description = "Policy for EKS cluster creation and management"
#   policy      = jsonencode({
#     Version = "2012-10-17"
#     Statement = [
#       {
#         Effect = "Allow"
#         Action = [
#           "eks:CreateCluster",
#           "eks:DeleteCluster",
#           "eks:DescribeCluster",
#           "eks:ListClusters",
#           "eks:UpdateClusterConfig",
#           "eks:UpdateClusterVersion",
#           "eks:CreateNodegroup",
#           "eks:DeleteNodegroup",
#           "eks:DescribeNodegroup",
#           "eks:ListNodegroups",
#           "eks:UpdateNodegroupConfig",
#           "eks:UpdateNodegroupVersion",
#           "ec2:DescribeVpcs",
#           "ec2:DescribeSubnets",
#           "ec2:DescribeSecurityGroups",
#           "ec2:CreateSecurityGroup",
#           "ec2:AuthorizeSecurityGroupIngress",
#           "ec2:AuthorizeSecurityGroupEgress",
#           "ec2:RevokeSecurityGroupIngress",
#           "ec2:RevokeSecurityGroupEgress",
#           "ec2:DescribeRouteTables",
#           "ec2:CreateRoute",
#           "ec2:DeleteRoute",
#           "ec2:DescribeInternetGateways",
#           "ec2:AttachInternetGateway",
#           "ec2:DetachInternetGateway",
#           "ec2:DescribeVpcPeeringConnections",
#           "ec2:CreateTags",
#           "ec2:DeleteTags",
#           "ec2:DescribeNetworkInterfaces",
#           "ec2:CreateNetworkInterface",
#           "ec2:DeleteNetworkInterface",
#           "ec2:DescribeInstances",
#           "ec2:RunInstances",
#           "ec2:TerminateInstances",
#           "ec2:DescribeLaunchTemplates",
#           "ec2:CreateLaunchTemplate",
#           "ec2:DeleteLaunchTemplate",
#           "ec2:DescribeImages",
#           "ec2:DescribeKeyPairs",
#           "ec2:ImportKeyPair",
#           "ec2:DescribeAvailabilityZones",
#           "ec2:DescribeSecurityGroupRules",
#           "ec2:CreateInternetGateway",
#           "ec2:CreateVpc",
#           "ec2:ModifyVpcAttribute",
#           "ec2:DescribeVpcAttribute",
#           "ec2:CreateRouteTable",
#           "ec2:CreateSubnet",
#           "ec2:CreateRouteTable",
#           "ec2:AllocateAddress",
#           "ec2:AssociateRouteTable",
#           "iam:CreateRole",
#           "iam:DeleteRole", 
#           "iam:AttachRolePolicy",
#           "iam:DetachRolePolicy",
#           "iam:PassRole",
#           "iam:CreatePolicy",
#           "iam:GetRolePolicy",
#           "iam:DeletePolicy",
#           "iam:CreateInstanceProfile",
#           "iam:AddRoleToInstanceProfile",
#           "iam:RemoveRoleFromInstanceProfile",
#           "iam:DeleteInstanceProfile",
#           "iam:GetRole",
#           "iam:ListRoles",
#           "iam:ListAttachedRolePolicies",
#           "autoscaling:CreateAutoScalingGroup",
#           "autoscaling:UpdateAutoScalingGroup",
#           "autoscaling:DeleteAutoScalingGroup",
#           "autoscaling:DescribeAutoScalingGroups",
#           "autoscaling:CreateLaunchConfiguration",
#           "autoscaling:DeleteLaunchConfiguration",
#           "autoscaling:DescribeLaunchConfigurations",
#           "autoscaling:CreateOrUpdateTags",
#           "autoscaling:DeleteTags",
#           "autoscaling:UpdateTags",
#           "elasticloadbalancing:CreateLoadBalancer",
#           "elasticloadbalancing:DeleteLoadBalancer",
#           "elasticloadbalancing:DescribeLoadBalancers",
#           "elasticloadbalancing:DescribeTargetGroups",
#           "elasticloadbalancing:CreateTargetGroup",
#           "elasticloadbalancing:DeleteTargetGroup",
#           "elasticloadbalancing:DescribeListeners",
#           "elasticloadbalancing:CreateListener",
#           "elasticloadbalancing:DeleteListener",
#           "cloudwatch:PutMetricAlarm",
#           "cloudwatch:DescribeAlarms",
#           "cloudwatch:DeleteAlarms",
#           "cloudwatch:GetMetricData",
#           "cloudwatch:ListMetrics",
#           "logs:CreateLogGroup",
#           "logs:CreateLogStream",
#           "logs:PutLogEvents",
#           "logs:DescribeLogGroups",
#           "logs:DescribeLogStreams",
#           "logs:DeleteLogGroup",
#           "logs:DeleteLogStream",
#           "logs:TagResource",
#           "logs:PutRetentionPolicy",
#           "logs:ListTagsLogGroup",
#           "s3:CreateBucket",
#           "s3:DeleteBucket",
#           "s3:ListBucket",
#           "s3:PutObject",
#           "s3:GetObject",
#           "s3:DeleteObject",
#           "s3:ListAllMyBuckets",
#           "sns:CreateTopic",
#           "sns:DeleteTopic",
#           "sns:Subscribe",
#           "sns:Unsubscribe",
#           "sns:Publish",
#           "sns:ListTopics",
#           "kms:TagResource",
#           "kms:CreateKey",
#           "kms:CreateAlias"

#         ]
#         Resource = "*"
#       }
#     ]
#   })
# }

resource "aws_iam_policy" "eks_policy" {
  name        = "EKSPolicy"
  description = "Policy for EKS cluster creation and management"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "ssm:GetParameter",
          #   "eks:CreateCluster",
          #   "eks:DeleteCluster",
          #   "eks:DescribeCluster",
          #   "eks:ListClusters",
          #   "eks:UpdateClusterConfig",
          #   "eks:UpdateClusterVersion",
          #   "eks:CreateNodegroup",
          #   "eks:DeleteNodegroup",
          #   "eks:DescribeNodegroup",
          #   "eks:ListNodegroups",
          #   "eks:UpdateNodegroupConfig",
          #   "eks:UpdateNodegroupVersion",
          #   "eks:TagResource",
          "ec2:DescribeVpcs",
          "ec2:DescribeSubnets",
          "ec2:DescribeSecurityGroups",
          "ec2:CreateSecurityGroup",
          "ec2:AuthorizeSecurityGroupIngress",
          "ec2:AuthorizeSecurityGroupEgress",
          "ec2:RevokeSecurityGroupIngress",
          "ec2:RevokeSecurityGroupEgress",
          "ec2:DescribeRouteTables",
          "ec2:CreateRoute",
          "ec2:DeleteRoute",
          "ec2:DescribeInternetGateways",
          "ec2:AttachInternetGateway",
          "ec2:DetachInternetGateway",
          "ec2:DescribeVpcPeeringConnections",
          "ec2:CreateTags",
          "ec2:DeleteTags",
          "ec2:DescribeNetworkInterfaces",
          "ec2:CreateNetworkInterface",
          "ec2:DeleteNetworkInterface",
          "ec2:DescribeInstances",
          "ec2:RunInstances",
          "ec2:TerminateInstances",
          "ec2:DescribeLaunchTemplates",
          "ec2:CreateLaunchTemplate",
          "ec2:DeleteLaunchTemplate",
          "ec2:DescribeImages",
          "ec2:DisassociateRouteTable",
          "ec2:DescribeKeyPairs",
          "ec2:ImportKeyPair",
          "ec2:DescribeAvailabilityZones",
          "ec2:DescribeSecurityGroupRules",
          "ec2:CreateInternetGateway",
          "ec2:CreateVpc",
          "ec2:ModifyVpcAttribute",
          "ec2:DescribeVpcAttribute",
          "ec2:CreateRouteTable",
          "ec2:CreateSubnet",
          "ec2:CreateRouteTable",
          "ec2:AllocateAddress",
          "ec2:AssociateRouteTable",
          "iam:CreateRole",
          "iam:DeleteRole",
          "iam:AttachRolePolicy",
          "iam:DetachRolePolicy",
          "iam:PassRole",
          "iam:TagRole",
          "iam:CreatePolicy",
          "iam:GetRolePolicy",
          "iam:DeletePolicy",
          "iam:CreateInstanceProfile",
          "iam:AddRoleToInstanceProfile",
          "iam:RemoveRoleFromInstanceProfile",
          "iam:GetInstanceProfile",
          "iam:DeleteInstanceProfile",
          "iam:GetRole",
          "iam:ListRoles",
          "iam:ListAttachedRolePolicies",
          "autoscaling:CreateAutoScalingGroup",
          "autoscaling:UpdateAutoScalingGroup",
          "autoscaling:DeleteAutoScalingGroup",
          "autoscaling:DescribeAutoScalingGroups",
          "autoscaling:CreateLaunchConfiguration",
          "autoscaling:DeleteLaunchConfiguration",
          "autoscaling:DescribeLaunchConfigurations",
          "autoscaling:CreateOrUpdateTags",
          "autoscaling:DeleteTags",
          "autoscaling:UpdateTags",
          "elasticloadbalancing:CreateLoadBalancer",
          "elasticloadbalancing:DeleteLoadBalancer",
          "elasticloadbalancing:DescribeLoadBalancers",
          "elasticloadbalancing:DescribeTargetGroups",
          "elasticloadbalancing:CreateTargetGroup",
          "elasticloadbalancing:DeleteTargetGroup",
          "elasticloadbalancing:DescribeListeners",
          "elasticloadbalancing:CreateListener",
          "elasticloadbalancing:DeleteListener",
          #   "cloudwatch:PutMetricAlarm",
          #   "cloudwatch:DescribeAlarms",
          #   "cloudwatch:DeleteAlarms",
          #   "cloudwatch:GetMetricData",
          #   "cloudwatch:ListMetrics",
          #   "logs:CreateLogGroup",
          #   "logs:CreateLogStream",
          #   "logs:PutLogEvents",
          #   "logs:DescribeLogGroups",
          #   "logs:DescribeLogStreams",
          #   "logs:DeleteLogGroup",
          #   "logs:DeleteLogStream",
          #   "logs:TagResource",
          #   "logs:PutRetentionPolicy",
          #   "logs:ListTagsLogGroup",
          #   "s3:CreateBucket",
          #   "s3:DeleteBucket",
          #   "s3:ListBucket",
          #   "s3:PutObject",
          #   "s3:GetObject",
          #   "s3:DeleteObject",
          #   "s3:ListAllMyBuckets",
          #   "sns:CreateTopic",
          #   "sns:DeleteTopic",
          #   "sns:Subscribe",
          #   "sns:Unsubscribe",
          #   "sns:Publish",
          #   "sns:ListTopics",
          #   "kms:TagResource",
          #   "kms:CreateKey",
          #   "kms:CreateAlias"
        ]
        Resource = "*"
      }
    ]
  })
  #   lifecycle {
  #       prevent_destroy = true
  #     }
}
# IAM Role for EKS Cluster
resource "aws_iam_role" "eks_role" {
  name = "EKSClusterRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "eks.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role" "ec2_role" {
  name = "Ec2role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "ec2_role_policy_attachment" {
  role       = aws_iam_role.ec2_role.name
  policy_arn = aws_iam_policy.eks_policy.arn
}

# Attach the Policy to the Role
# resource "aws_iam_role_policy_attachment" "eks_role_policy_attachment" {
#   role       = aws_iam_role.eks_role.name
#   policy_arn = aws_iam_policy.eks_policy.arn
# }

# resource "aws_iam_user_policy_attachment" "eks_user_policy_attachment" {
#   user      = "ctwo"
#   policy_arn = aws_iam_policy.eks_policy.arn
#   lifecycle {
#       prevent_destroy = true
#     }
# }
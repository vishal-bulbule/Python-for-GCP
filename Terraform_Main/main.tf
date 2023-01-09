# module "create_bucket" {
#   source = "./storage"
#   project-id = "gcp-d-p"
#   region = "us"
# }

# module "alert" {
# source = "./alerts"
# project-id = var.project
# slack_channel = var.slack_channel
# }


module "iam" {
source = "./IAM"
project = var.project
}
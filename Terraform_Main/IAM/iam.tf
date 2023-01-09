# resource "google_project_iam_member" "project-role" {
#   project = var.project-id
#   role = "roles/editor"
#   member = var.Users
# }

#Creating service account
resource "google_service_account" "composer" {
  account_id   = "composer-env-account"
  display_name = "Test Service Account for Composer Environment"
}

#Assigning permission to SA
resource "google_project_iam_member" "composer-worker" {
  project = var.project
  role    = "roles/composer.worker"
  member  = "serviceAccount:${google_service_account.composer.email}"
  depends_on = [
    google_service_account.composer
  ]
}

# resource "google_project_iam_member" "composer-sa" {
#   project = var.project-id
#   role    = "roles/iam.serviceAccountUser"
#   member  = "serviceAccount:${google_service_account.composer.email}"
#   depends_on = [
#     google_project_iam_member.composer-worker
#   ]
# }


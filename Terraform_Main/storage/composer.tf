resource "google_composer_environment" "prod" {
  name   = "composer-prod"
  region = var.composer-region
  config {

    software_config {
      image_version = "composer-2-airflow-2"
    }

    workloads_config {
      scheduler {
        ##cpu        = 2
        #memory_gb  = 3.25
        storage_gb = 5
        count      = 2
      }
      web_server {
        #cpu        = 2
        #memory_gb  = 3.25
        storage_gb = 5
      }
      worker {
        #cpu = 3
        #memory_gb  = 
        storage_gb = 5
        min_count  = 2
        max_count  = 6
      }


    }
    environment_size = "ENVIRONMENT_SIZE_MEDIUM"

    node_config {
      network    = var.network_id
      subnetwork = var.composer_subnetwork
      service_account = google_service_account.composer.name
    }
  }
  depends_on = [
    google_project_iam_member.composer-sa
  ]
}
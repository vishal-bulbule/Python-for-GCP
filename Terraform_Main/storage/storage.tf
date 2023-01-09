resource "google_storage_bucket" "terraform-test" {
  name = "bkt-poc-terraform"
  project = var.project-id
  storage_class = "STANDARD"
  location = var.region
  versioning {
    enabled = true
  }
  uniform_bucket_level_access = true
  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }
  logging {
    log_bucket = "log"
  }

}



resource "google_storage_bucket_object" "object" {
  name   = "folder/key.json"
  source = "key.json"
  content_type = "application/octet-stream"
  bucket = google_storage_bucket.terraform-test.name
}
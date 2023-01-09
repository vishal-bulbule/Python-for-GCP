resource "google_compute_network" "demp-vpc" {
    name = "demo-vpc"
    auto_create_subnetworks = false
    project = "gcp-d-p"
}

resource "google_compute_subnetwork" "us-east4" {
    name = "subnet-useast4"
    project = "gcp-d-p"
    region = "us-east4"
    network = google_compute_network.demp-vpc.self_link
    ip_cidr_range = "10.10.0.0/28"
}

resource "google_compute_subnetwork" "us-west4" {
    name = "subnet-uswest4"
    project = "gcp-d-p"
    region = "us-west4"
    network = google_compute_network.demp-vpc.self_link
    ip_cidr_range = "10.10.10.0/28"

}
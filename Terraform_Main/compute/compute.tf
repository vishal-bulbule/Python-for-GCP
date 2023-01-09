# resource "google_compute_instance" "vm-module" {
#   name         = "test-vm"
#   machine_type = "e2-small"
#   zone         = var.zone
#   tags         = ["demo", "test"]

#   allow_stopping_for_update = true
#   service_account { 
#     email  = var.sa-compute
#     scopes = ["cloud-platform"]
#   }

#   boot_disk {
#     initialize_params {
#       image = "debian-cloud/debian-9"
#     }
#   }


#   network_interface {
#     subnetwork = var.subnetwork_id
#     network    = var.network_id
#   }
# }
#     /* 
#    ##########Remove access config block to create vm without external IP
#    access_config {
#       // Ephemeral public IP
#       nat_ip = null      
#     }
#   */

#   /*
#   }
#   metadata = {
#     enable-oslogin = true
#   }
# }
# */
# /*Changing the machine_type, min_cpu_platform, service_account, enable_display, 
#   shielded_instance_config, scheduling.node_affinities or network_interface.[#d].
#   (network/subnetwork/subnetwork_project) or advanced_machine_features on a started instance 
#   requires stopping it. To acknowledge this, please set allow_stopping_for_update = true 
#   in your config. You can also stop it by setting desired_status = "TERMINATED",
#    but the instance will not be restarted after the update.   */

# resource "google_compute_disk_resource_policy_attachment" "attachment" {
#   name = "mytrapture-schedule"
#   disk = google_compute_instance.vm-module.name
#   zone = var.zone

#   depends_on = [
#     google_compute_instance.vm-module
#   ]
# }
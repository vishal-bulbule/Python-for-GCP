resource "google_monitoring_alert_policy" "alert_policy" {
  display_name = "App Engine Alerts"
  project = var.project-id
  combiner     = "OR"
  conditions {
    display_name = "GAE Alert!!"
    condition_matched_log {
      filter = "resource.type = \"gae_app\" AND\nseverity >= (NOTICE OR WARNING OR ERROR OR CRITICAL OR ALERT OR EMERGENCY)"
      }
    }
 alert_strategy {
    notification_rate_limit {
      period = "360s"
    }
 }
  notification_channels= [var.slack_channel]
  
}
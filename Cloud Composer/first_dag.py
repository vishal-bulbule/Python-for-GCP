"""
Added comments wherever required
Please replace parameters for project,instance names,zone etc.
"""

import airflow
from airflow import DAG
from datetime import timedelta
from airflow.operators.bash_operator import BashOperator


default_args = {
    'start_date': airflow.utils.dates.days_ago(0),
    'retries': 0,
    #'retry_delay': timedelta(minutes=5)
}

#initialize dag
dag = DAG(
    'db_backup',
    default_args=default_args,
    description='Database backup',
    schedule_interval=None,
    dagrun_timeout=timedelta(minutes=20))

#Create first task to stop VM
stopvm = BashOperator(
    task_id='stopvm',
    bash_command='gcloud compute instances stop database --zone=us-central1-a',
    dag=dag,
    depends_on_past=False,
    do_xcom_push=False)

#Create 2nd task to create machine image
create_image = BashOperator(
    task_id='create_image',
    bash_command='gcloud compute machine-images create databaseimage --source-instance=database --source-instance-zone=us-central1-a',
    dag=dag,
    depends_on_past=False,
    do_xcom_push=False)

#Create 3rd task to start vm
start_vm = BashOperator(
    task_id='start_vm',
    bash_command='gcloud compute instances start database --zone=us-central1-a',
    dag=dag,
    depends_on_past=False,
    trigger_rule = 'one_success',
    do_xcom_push=False)

#Create 4th task to create snapshot vm
create_snapshot = BashOperator(
    task_id='create_snapshot',
    bash_command='gcloud compute snapshots create databasesnapshot --source-disk=database --source-disk-zone=us-central1-a',
    dag=dag,
    depends_on_past=False,
    trigger_rule = 'one_failed',
    do_xcom_push=False)

#Dependencies

stopvm >> create_image >> start_vm
create_image >> create_snapshot
create_snapshot >> start_vm

# First Dag, testing everything works and I am able to see the DAG in the UI when connected to it

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
from airflow.utils.dates import days_ago

# Simple Hello World

def hello_world():
    print ('Hello World!')

default_args = {
    'owner' : 'Luis',
    'start_date' : days_ago(0),
    'retries' : 1,
    'retry_delay': timedelta(minutes = 1),
}

dag = DAG(
    dag_id = 'hello_world_dag',
    default_args = default_args,
    description = 'A simple Hello World DAG',
    schedule_interval = None,
)

# Python task
task_hw = PythonOperator(
    task_id='say_hello_world',
    python_callable= hello_world,
    dag=dag, #which dag it belongs to
)

# Task to call
task_hw
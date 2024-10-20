from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'Adarsh',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 20),  # Adjust this as needed
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'test_dag',
    default_args=default_args,
    description='A simple test DAG',
    schedule_interval='0 9 * * *',  # Schedule: Every day at 9:00 AM
    catchup=False
)

# Task 1: Dummy task
start_task = DummyOperator(
    task_id='start_task',
    dag=dag
)

# Task 2: Python task for testing
def print_hello():
    print("Hello, Airflow!")

python_task = PythonOperator(
    task_id='python_task',
    python_callable=print_hello,
    dag=dag
)

# Task 3: End dummy task
end_task = DummyOperator(
    task_id='end_task',
    dag=dag
)

# Task dependencies
start_task >> python_task >> end_task

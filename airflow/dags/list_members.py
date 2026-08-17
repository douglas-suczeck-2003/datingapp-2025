from airflow import DAG
from airflow.providers.microsoft.mssql.hooks.mssql import MsSqlHook
from airflow.operators.python import PythonOperator

from datetime import datetime


def list_members():
    hook = MsSqlHook(
        mssql_conn_id="dating_sql"
    )

    members = hook.get_records(
        "SELECT DisplayName FROM Members"
    )

    print("MEMBERS:")

    for member in members:
        print(member[0])


with DAG(
    dag_id="list_dating_members",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    list_members_task = PythonOperator(
        task_id="list_members",
        python_callable=list_members,
    )
from airflow import DAG
from airflow.providers.microsoft.mssql.hooks.mssql import MsSqlHook
from airflow.operators.python import PythonOperator

from datetime import datetime


def count_likes():
    hook = MsSqlHook(
        mssql_conn_id="dating_sql"
    )

    result = hook.get_first(
        "SELECT COUNT(*) FROM Likes"
    )

    print(f"AMOUNT OF LIKES: {result[0]}")


with DAG(
    dag_id="count_dating_likes",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    count_likes_task = PythonOperator(
        task_id="count_likes",
        python_callable=count_likes,
    )
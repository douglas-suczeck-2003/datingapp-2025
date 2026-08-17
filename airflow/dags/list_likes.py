from airflow import DAG
from airflow.providers.microsoft.mssql.hooks.mssql import MsSqlHook
from airflow.operators.python import PythonOperator
from datetime import datetime

def list_likes():
    hook = MsSqlHook(
        mssql_conn_id="dating_sql"
    )

    query = """
        SELECT
            SourceMember.DisplayName AS Liker,
            TargetMember.DisplayName AS Liked
        FROM Likes
        INNER JOIN Members AS SourceMember
            ON Likes.SourceMemberId = SourceMember.Id
        INNER JOIN Members AS TargetMember
            ON Likes.TargetMemberId = TargetMember.Id
        ORDER BY SourceMember.DisplayName
    """

    likes = hook.get_records(query)

    for liker, liked in likes:
        print(f"{liker} liked {liked}")


with DAG(
    dag_id="list_dating_likes",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    list_likes_task = PythonOperator(
        task_id="list_likes",
        python_callable=list_likes,
    )
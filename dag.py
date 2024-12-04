from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch


# Fungsi untuk Task 1
def fetch_from_postgresql():
    """
    Fungsi ini ditujukan untuk mengambil data dari tabel table_m3 dari database postgres dari PostgreSQL.

    Parameters: None

    Return: Dataframe berisikan data project yang bbersifat raw
        
    Contoh penggunaan:
    data = fetch_from_postgresql()
    """
    pg_hook = PostgresHook(
        postgres_conn_id='postgres_default',
    )
    query = 'SELECT * FROM postgres.table_m3;'
    df = pg_hook.get_pandas_df(sql=query)
    return df



# Fungsi untuk Task 2
def data_cleaning(**kwargs):
    """
    Fungsi ini ditujukan untuk melakukan pembersihan data, diantara lain:
    Menghilangkan duplikat
    Mengkecilkan huruf
    Mengubah spasi menjadi garis bawah
    Menghilangkan simbol dan whitespace
    Mengatasi missing values

    Parameters: Dataframe yang bersifat raw atau mentah

    Return: Dataframe yang bersifat clean atau bersih
        
    Contoh penggunaan:
    data = data_cleaning(df)
    """

    df = kwargs['ti'].xcom_pull(task_ids='fetch_from_postgresql')

    # Menghilangkan baris data duplikat
    df = df.drop_duplicates()

    # Mengkecilkan huruf pada header
    df.columns = df.columns.str.lower()

    # Mengubah spasi menjadi simbol garis bawah pada header
    df.columns = df.columns.str.replace(' ', '_')

    # Menghilangkan whitespace pada header
    df.columns = df.columns.str.strip()

    # Menghilangkan simbol kecuali simbol garis bawah pada header
    df.columns = df.columns.str.replace(r'[^\w_]', '', regex=True)

    # Mengatasi missing values
    for column in df.columns:
        if df[column].dtype == 'object':
            # Melakukan imputasi missing values dengan mode jika kolom bertipe kategorikal
            df[column].fillna(df[column].mode()[0], inplace=True)
        else:
            # Melakukan imputasi missing values dengan median jika kolom bertipe numerikal
            df[column].fillna(df[column].median(), inplace=True)

    df.to_csv('/opt/airflow/data/P2M3_nuzul_data_clean.csv', sep=',', index=False)
    return df

# Fungsi untuk Task 3
def post_to_elasticsearch(**kwargs):
    """
    Fungsi ini ditujukan untuk memasukkan dataframe ke dalam database elasticsearch

    Parameters: Dataframe yang bersifat clean atau bersih

    Return: Kondisi dataframe yang berada di elasticsearch
        
    Contoh penggunaan:
    data = post_to_elasticsearch(df)
    """

    df = kwargs['ti'].xcom_pull(task_ids='data_cleaning')

    # Inisialisasi koneksi dengan elasticsearch
    es = Elasticsearch("http://localhost:9200") 

    # Melakukan iterasi per masing-masing baris data
    for i,r in df.iterrows():
        # Ubah ke dalam json
        doc=r.to_json()
        # Memasukkan data ke elasticsearch dengan index frompostgresql
        res=es.index(index="data_milestone3", doc_type="doc", body=doc)


with DAG('milestone3',
         default_args={'owner': 'nuzul',
                       'start_date': datetime(2024, 11, 11, 23, 30),  # UTC time, adjust as needed
                       'retries': 1,
                       'retry_delay': timedelta(minutes=1),
                       },
         schedule_interval=timedelta(days=1)
         ) as dag:
    
    fetch_from_postgresql_task = PythonOperator(task_id='fetch_from_postgresql',
                                  python_callable=fetch_from_postgresql,
                                  provide_context=True,
                                  dag=dag)
    
    data_cleaning_task = PythonOperator(task_id='data_cleaning',
                                        python_callable=data_cleaning,
                                        provide_context=True,
                                        dag=dag)
    
    post_to_elasticsearch_task = PythonOperator(task_id='post_to_elasticsearch',
                                        python_callable=post_to_elasticsearch,
                                        provide_context=True,
                                        dag=dag)
    
    

fetch_from_postgresql_task >> data_cleaning_task >> post_to_elasticsearch_task

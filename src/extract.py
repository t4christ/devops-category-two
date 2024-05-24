import os
import pandas as pd
from sqlalchemy import create_engine

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = "5432"
DB_NAME = os.environ.get('DB_NAME')

table_name = os.environ.get('TABLE_NAME')

def extract_data():
    # Create the database connection
    db_url = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    engine = create_engine(db_url)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, engine)
    return df
import os
from transform import transform_data
from extract import extract_data
from sqlalchemy import create_engine

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = "5432"
DB_NAME = os.environ.get('DB_NAME')

cleaned_data_table_name = os.environ.get('CLEANED_TABLE_NAME')


def load_data(data):
    print("")
    print("")
    print("Load Cleaned Data To Database")
    print("--------------------")

    try:
        db_url = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        engine = create_engine(db_url)
        data.to_sql(cleaned_data_table_name, engine, if_exists='replace', index=False)
        print("Successfully loaded cleaned data into database")
    except Exception as e:
        print(f"Error loading cleaned data into db {e}")
        sys.exit(1)

if __name__ == "__main__":
    cleaned_data = transform_data(extract_data())
    load_data(cleaned_data)
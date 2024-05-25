import os
import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = "5433"
DB_NAME = os.environ.get('DB_NAME')

table_name = os.environ.get('TABLE_NAME')


# Create the database connection
db_url = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(db_url)


# Read the Excel file
excel_file_path = 'bondmovie.xlsx'
df = pd.read_excel(excel_file_path)

# Ensure the DataFrame matches the database table structure
print(df.head())  # Optional: Check the first few rows of the DataFrame

# Load the data into the PostgreSQL table
df.to_sql(table_name, engine, if_exists='replace', index=False)

print("Data loaded successfully.")

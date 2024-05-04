#!/bin/bash

# Check if the required environment variables are set
if [ -z "$DB_USER" ]; then
  echo "ERROR: DB_USER environment variable is not set."
  exit 1
fi

if [ -z "$DB_PASS" ]; then
  echo "ERROR: DB_PASS environment variable is not set."
  exit 1
fi

# Create a new DBQL user with the provided username and password
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
  CREATE USER "$DB_USER" WITH PASSWORD '$DB_PASS';
  ALTER USER "$DB_USER" WITH SUPERUSER;
  CREATE DATABASE "$DB_NAME";
EOSQL

echo "Initialization completed successfully."
FROM postgres:latest

COPY infrastructure/docker/postgres/init-db.sh /docker-entrypoint-initdb.d/
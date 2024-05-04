FROM postgres

COPY infrastructure/docker/db/init-db.sh /docker-entrypoint-initdb.d/

COPY infrastructure/docker/db/task.sql /docker-entrypoint-initdb.d/
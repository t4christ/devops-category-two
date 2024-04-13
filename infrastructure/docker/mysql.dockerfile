# Use official MySQL image as the base image
FROM mysql:latest


COPY db/silky_structure.sql /docker-entrypoint-initdb.d/
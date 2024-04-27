# Use an official Python runtime as a parent image
FROM python:3.10-alpine as base

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# Install run-time dependencies that are needed permanently in the image  
RUN apk add --no-cache \
    libpq \
    libmagic

# Install build-time dependencies which are needed only during the build process and removed after
RUN apk add --no-cache --virtual .build-deps \
    build-base \
    postgresql-dev \
    python3-dev \
    file-dev && \
    # Upgrade pip to the latest version, Preparing the Environment for whatever dependencies required
    pip3 install --upgrade pip && \
    adduser -D -g "" -H -s "/sbin/nologin" -u 10001 goldenuser

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt 

# Cleanup: After installing dependencies, remove build-time packages to reduce image size
RUN apk del .build-deps

COPY . .
RUN chown -R goldenuser:goldenuser start.sh && chmod +x start.sh

USER goldenuser

EXPOSE 8009

ENTRYPOINT ["./start.sh"]


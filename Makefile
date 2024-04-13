# Read credentials from the file
include mysql-credentials.txt

# Define the build arguments
BUILD_ARGS ?= MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD} MYSQL_DATABASE=${MYSQL_DATABASE}  MYSQL_USER=${MYSQL_USER}  MYSQL_PASSWORD=${MYSQL_PASSWORD} 

# Default target
.PHONY: all
all: run down down_volume

# Target to build the containers with build arguments
.PHONY: build

.SILENT: run 

run:
	$(BUILD_ARGS) docker-compose up -d --build
down:
	 docker-compose down --remove-orphans 

down_volume:
	 docker-compose down --remove-orphans --volumes
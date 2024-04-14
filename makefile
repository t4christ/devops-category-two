# Default target
.PHONY: all
all: run down down_volume

# Target to build the containers with build arguments
.PHONY: build

.SILENT: run 

run:
	 docker-compose up -d --build
down:
	 docker-compose down --remove-orphans 

down_volume:
	 docker-compose down --remove-orphans --volumes


down_app:
	docker-compose down app --remove-orphans
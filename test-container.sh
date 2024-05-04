#!/bin/bash

test_docker_container(){
local image="$1"

echo "Running docker container"
 IMAGE=$image docker-compose up -d --build --remove-orphans
if [ $? -eq 0 ]; then
    echo "Docker run execution succeeded"

    sleep 5

    http_status=$(curl -s -o /dev/null -w "%{http_code}" localhost:3500/health)
    
    if [ "$http_status" -eq 200 ]; then
        echo "Http status code is 200."
        curl localhost:3500/health

        docker-compose down --volume
        echo "Container killed successfully"

        exit 0
    else
        echo " Http status code not ok. request failed"
        curl localhost:3500/health
        exit 1
    fi
    exit 0
else
    echo " Command execution failed"
    exit 1
fi
}

echo "Running test container function"
test_docker_container $1
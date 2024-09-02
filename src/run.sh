#!/bin/bash

IMAGE_NAME="web_launcher"
IMAGE_TAG="1.0"
CONTAINER_NAME=${IMAGE_NAME}

HOST_PORT=8000
CONTAINER_PORT=8000

echo "Building Docker image..."
DOCKER_IMAGE_BUILD_EXIT_CODE=$(docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .; echo $?)

if [ "${DOCKER_IMAGE_BUILD_EXIT_CODE}" -ne 0 ]; then
    echo "Docker image build failed. Exiting."
    exit 1
fi

if [ "$(docker ps -aq -f name=${CONTAINER_NAME})" ]; then
    echo "Stopping and removing existing container..."
    docker stop ${CONTAINER_NAME}
    docker rm ${CONTAINER_NAME}
fi

echo "Running Docker container..."
DOCKER_CONTAINER_RUN_EXIT_CODE=$(docker run -d --name ${CONTAINER_NAME} -p ${HOST_PORT}:${CONTAINER_PORT} ${IMAGE_NAME}:${IMAGE_TAG}; echo $?)

if [ "${DOCKER_CONTAINER_RUN_EXIT_CODE}" -eq 0 ]; then
    echo "Container ${CONTAINER_NAME} is up and running!"
    echo "Access the application at http://localhost:${HOST_PORT}"
else
    echo "Failed to start the container. Exiting."
    exit 1
fi

#!/bin/bash

docker build -t "repo.treescale.com/thomas_michelet/deploy-container" .
echo "$DOCKER_PASSWORD" | docker login --username "$DOCKER_USERNAME" --password-stdin repo.treescale.com
docker push "repo.treescale.com/thomas_michelet/deploy-container"

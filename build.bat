@echo off
REM Stop the current running containers
docker-compose down

REM Remove dangling images
docker image prune -f

docker build -f Docker/bigdataspark -t bigdataspark .
docker build -f Docker/bigdatakafka -t bigdatakafka .
docker build -f Docker/bigdatadash -t bigdatadash .

REM Start the services with the new image
docker-compose up --build -d

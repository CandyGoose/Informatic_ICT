#!/bin/bash

# Получаем ID контейнера с именем "webserver"
id=$(sudo docker container ls --all --quiet --filter "name=webserver")

# Запускаем интерактивную оболочку bash внутри контейнера с указанным ID
docker exec -it $id bash

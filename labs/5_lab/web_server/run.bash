#!/bin/bash

# Запускаем новый контейнер с именем "webserver"
# -d: Запускает контейнер в фоновом (detach) режиме
# -p 80:80: Пробрасываем порт 80 контейнера на порт 80 хоста
# server-image: Используем образ с именем "server-image" для создания контейнера
docker run --name webserver -d -p 80:80 server-image

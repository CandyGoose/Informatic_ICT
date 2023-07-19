# Используем базовый образ Ubuntu с тегом "latest"
FROM ubuntu:latest

# Обновляем список пакетов в репозитории
RUN apt-get update

# Устанавливаем пакет Apache HTTP Server
RUN apt-get install -y apache2

# Открываем порт 80 для доступа к веб-серверу
EXPOSE 80

# Создаем простую HTML-страницу и копируем ее в директорию /var/www/html/
RUN echo "<html> <head>   <title> I love Docker! </title> </head> <body>  <p> Hello world! I'm Vera and I study at ITMO University! </p> </body> </html>" > /var/www/html/index.html

# Запускаем Apache в режиме FOREGROUND при запуске контейнера
CMD ["apache2ctl", "-D", "FOREGROUND"]

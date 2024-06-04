# Как запустить лабу?
1) Установите Docker и Apache, последовательно выполнив команды

```
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo apt update
sudo apt install apache2
```

2) Перейдите в папку, где лежит докерфайл и скрипты
3) Пропишите
```
sudo bash build.bash
```
4) Далее, если не возникло ошибок
```
sudo bash run.bash
```
__Возможные ошибки на данном этапе:__

- docker: Error response from daemon: driver failed programming external connectivity on endpoint webserver (5975254dd2a6506bac39651fe30178b3e679e8a99ac4acdd669930709ea654f3): Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use.
- docker: Error response from daemon: Conflict. The container name "/webserver" is already in use by container "fc743abba3a29d3c749bcac5f4032c2488bb6c7f30993ada50e43ed4c7a1e0a1". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'.

__Решение:__
```
sudo service apache2 stop
sudo docker container prune
```
Если вторая ошибка не исчезает, то напишите команду:
```
sudo docker container ls
```
![image](https://github.com/CandyGoose/Informatic_ICT/assets/112972833/fbbef553-ea17-4e7f-8d2a-c44ec93af5b1)
Появятся такие записи. Теперь необходимо прописать следующие команды:
```
sudo docker stop webserver
sudo docker rm webserver
```
где webserver это имя контейнера из NAMES.

После этого еще раз напишите:
```
sudo bash run.bash
```
5) Зайдите в браузер на виртуальной машине и наберите в поиске `localhost`. Должна появиться следующая страница:

![image](https://github.com/CandyGoose/Informatic_ICT/assets/112972833/4b74f9ba-9725-4277-947d-f1a671108a80)

6) Возвращается в терминал и прописываем:
```
sudo bash exec.bash
```
![image](https://github.com/CandyGoose/Informatic_ICT/assets/112972833/cdffffe0-1009-471f-8ce9-4adcd0792c62)

Чтобы выйти отсюда достаточно написать `exit`

Готово! Лаба сделана.

## Как это примерно выглядело у меня:

![pic](https://github.com/CandyGoose/Informatic_ICT/assets/112972833/5620aa3b-e044-4f62-b4d7-7d286187a3cb)

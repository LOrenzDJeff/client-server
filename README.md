## Команды для того, что бы запускать докеры 
- что бы запустить только проект, без теста:

```
sudo docker-compose up --scale test3=0 --build
```

- что бы запустить только проект и несколько клиентов:

```
sudo docker-compose up --scale test3=0 --scale client=N --build
```

- что бы запустить тест:

```
sudo docker-compose up --scale client=0 --scale server=0 --build

```

- После изменения Дениса:

```
sudo docker-compose up --scale client=0 --build

```

- что бы зайти в консоль контейнера:

```
docker exec -it serv sh -c "./sc.sh"
```


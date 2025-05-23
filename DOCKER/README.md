<div style="text-align: center">
    <h1>DOCKER</h1>
</div>


<details> 
    <summary>Установка</summary>

1. Скачиваем и устанавдиваем [докер](https://www.docker.com/) 
2. После нужно установить [WLS](https://docs.docker.com/desktop/setup/install/windows-install/) `wsl --install`
3. в Bios для AMD включить виртуализацию Advance -> SVM Mode
</details>

<details> 
    <summary>Базовые команды работы с образами и контейнерами</summary>

*        Всместо <имя конейнера> удобнее использовать <ID образа>
* `docker run --help` - посмотреть команды , разные флаги
* `docker images` - список образов
* `docker pull <имя образа>` - скачать образ
* `docker run <имя образа>` - запустить/создать контейнер по стандарту применяется TAG (<имя образа>:<TAG>)
* `docker run <имя образа>:<TAG>` - как и вариант выше, запустить/создать контейнер с рандомным именем
* `docker run --name <имя конейнера>:<TAG>` - запустить/создать контейнер с заданным именем
* `docker run --rm <имя образа>:<TAG>` - запустить/создать контейнер с удалением после завершения
* `docker ps` - список запущенных контейнеров
* `docker ps -a` - весь список контейнеров
* `docker start <имя конейнера>` - запустить уже созданный контейнер
* `docker start -i <имя конейнера>` - запустить уже созданный контейнер в интерактивном режиме(выводит в терминал)
* `docker start -t <имя конейнера>` - -t (или --attach): Этот флаг указывает Docker подключиться к терминалу контейнера
  после его запуска. Это позволяет вам взаимодействовать с контейнером в интерактивном режиме, как если бы вы запускали
  его с помощью docker run -it
* `docker start -i -t <имя конейнера>` - комплексная команда для запуска контейнера в интерактивном режиме
* `docker stop <имя конейнера>` - остановить контейнер
* `docker kill <имя конейнера>` - убить контейнер
* `docker rmi <имя образа>` - удалить образ
* `docker rm <имя конейнера>` - удалить контейнер
* `docker container prune` - удалить все неиспользуемые контейнеры

</details>

<details> 
    <summary>Satus</summary>

* `Exited (0)`: контейнер завершил работу нормально
* `Exited (137)`: контейнер завершил работу с ошибкой
</details>


<details> 
    <summary>Примеры</summary>

* `docker run --name test -it python:3.12-alpine`

* `docker build  . -t myapp:0.1` -создание образа с именем myapp и тегом 0.1
```dockerfile
FROM python:3.12-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /python-app
COPY . .
CMD ["python", "main.py"]
```
`ENV PYTHONUNBUFFERED=1` для отключениея буфера
</details>

<details> 
    <summary>Создание</summary>

* `docker build <путь к DockerFile> -t <имя образа> .`

</details>



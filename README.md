# yamdb_final

![Deploy badge](https://github.com/Junior-George/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)


### Создание и запуск образа 

 

* * Создание и запуск образа не обходимо выполнять в директории с файлом Dockerfile 

 

* Для создания образа необхадимо выполнить следующую комманду. '<название образа>'

docker build -t <название образа> .  

 

* Далее необходимо запустить образ. Название контейнера выбирается самостоятельно 

docker run --name <имя контейнера> -it -p 8000:8000 <название образа> 

 

* * После этого образ будет доступен по ссылке в браузере localhost:8000 

 

 

### Создание и запуск web контейнера nginx 

 

* * Создание и запуск контейнера не обходимо выполнять в директории с файлом docker-compose.yaml 

 

* Для сборки контейнера необхадимо выполнить следующую комманду. '<название образа>'

docker-compose up -d --build 

 

* Далее необходимо сделать миграции 

docker-compose exec web python manage.py migrate 

 

* Создаем супер-пользователя 

docker-compose exec web python manage.py createsuperuser 

 

* Создаем статику 

docker-compose exec web python manage.py collectstatic --no-input 

 

* * После этого образ будет доступен по ссылке в браузере http://localhost/, админка по ссылке http://localhost/admin/
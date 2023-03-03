# yamdb_final

![Deploy badge](https://github.com/Junior-George/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

 

### Создание и запуск контейнеров

 

* * Создание и запуск контейнеров не обходимо выполнять в директории с файлом docker-compose.yaml 

 

* Для сборки контейнеров необхадимо выполнить следующую комманду

docker-compose up -d --build 

 

* Далее необходимо сделать миграции 

docker-compose exec web python manage.py migrate 

 

* Создаем супер-пользователя 

docker-compose exec web python manage.py createsuperuser 

 

* Добавляем статику 

docker-compose exec web python manage.py collectstatic --no-input 

 

* * После этого образ будет доступен по ссылке в браузере http://localhost/, админка по ссылке http://localhost/admin/


### Остановка контейнеров

* * Остановку контейнеров не обходимо выполнять в директории с файлом docker-compose.yaml 

* Команда для остановки контенеров 

docker-compose down -v

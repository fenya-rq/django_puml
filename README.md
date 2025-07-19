# Тестовое задание на проверку 

Проверяется умение работать с Django (models, DRF) и аналитическими артефактами (UML диаграмм, C4)

1. Создать django-проект Backend и в нем приложение Plan
2. Реализовать вариант использования **Сохранить объем работ** в **заданной архитектуре**
3. Подготовить docker-compose для запуска
4. Результат разместить в публичном git-репозитории

___

#### <p align="center">Run project</p>

> Pre-requisites: Docker >=28.3.0 installed.

Clone and run the project locally:

1. Clone the repository:

    `git clone https://github.com/fenya-rq/django_puml.git`

2. Change directory:

    `cd django_puml`

3. Copy example environment files:

    `cp .env.example .env; cp src/core/.env.example src/core/.env`

4. Adjust the .env in project root - need add your own Django secret key.
5. Start the project:

    `docker compose up -d`

___
#### <p align="center">Testing functional</p>
> NOTE: 1 admin-user, 5 regular user, 4 factories and 4 fctory_users will be created while migrating 

1. Go to admin panel and assign needed group to users (admin user creds defined  in .env file):

   `http://localhost:8080/admin`

2. Next go to browsable API page:

   `http://localhost:8080/api/work-volume-list`

3. Log in with needed regular user and send request:
```json
{
  "factory": 1,
  "start": "2025-07-09",
  "finish": "2025-07-17",
  "weight": 21
}
```
___
#### <p align="center">Check Clickhouse records</p>
> If you want check record from Clickhouse:
> open terminal and insert command 
   `docker exec -it ch_db sh`,
> then `clickhouse-client --query "SELECT * FROM work_volume_record"`
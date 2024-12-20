# DRF-service

## Description:
Small service made using DRF and PostgreSQL, and docker.

## Goals:
1. Микросервис должен реализовывать минимум 4 запроса. Метод запроса (GET/POST/UPDATE/PATCH/DELETE) не важен.
2. Реализовывать микросервис можно на любом удобном языке (Python)
3. Необходимо использовать реляционную СУБД (PostgreSQL). 
4. Микросервис и СУБД должны развертываться совместно. Работать должны в контейнере. Для котейнеризации использовать Docker. 
5. Для конфигурирования использоваться docker-compose. Необходимо использовать multi-stage.
6. Проект должен быть размещено в gitlab/github с доступом для  выполнения операции clone или fork.
7. Для проверки работы необходимо использовать Postman. 
8. Требования к обработке ошибок: 
- при некорректных данных в запросе, микросервис не должен "падать", а возвращать http-код соответствующей ошибки и сопроводительное сообщение. 
- ОПЦИОНАЛЬНО. Логирование ошибок и действий в микросервисе.
9. ОПЦИОНАЛЬНО. Если кому-то хочется чуть глубже копнуть в микросервисную разработку, то рекомендую ознакомится со Swagger для документирования API. 

## Main URLs
1. api_main: http://127.0.0.1:8000
2. primarchs: http://127.0.0.1:8000/primarchs/
3. chapters: http://127.0.0.1:8000/chapters/
4. swagger API: http://127.0.0.1:8000/api/schema/swagger/

## Tools:
* `Django REST framework`
* `Docker`
* `PostgreSQL`

## Authors
[Alex Survilov](https://github.com/No1CareZ)

## License
[MIT](https://choosealicense.com/licenses/mit/)

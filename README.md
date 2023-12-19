# Diplom_Elokhin_Semen

В проекте представлены:

SQL-запросы для получения данных из БД Яндекс Самокат; Автотест к API; Скриншот с запуском теста в PyCharm.

Информация по запуску тестов: Для запуска тестов должны быть установлены пакеты pytest и requests Запуск всех тестов выполянется командой pytest

SQL запросы Задание 1 Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных. Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).
SELECT "Couriers".login,
COUNT(*)
FROM "Couriers"
INNER JOIN "Orders" ON "Couriers".id = "Orders"."courierId"
WHERE "Orders"."inDelivery" = true
GROUP BY "Couriers".login;
Ссылка на скриншот выполненого запроса: https://drive.google.com/file/d/1Sd7fUcTY55PixA6Igjit86mhCHBAVVP_/view?usp=sharing

Задание 2 Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно. Для этого: выведи все трекеры заказов и их статусы.
SELECT track,
   CASE
          WHEN finished=true THEN 2
          WHEN cancelled=true THEN -1
          WHEN "inDelivery"=true THEN 1
      ELSE 0
      END as status_zakaza
 FROM "Orders";
Ссылка на скриншот выполненого запроса: https://drive.google.com/file/d/16g9Y0cXFiAh9PAo6uIy94p95OxsO8rcc/view?usp=sharing
Технические примечания: Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. Пароль: smith. У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, select * from “Orders”.

Задание 3. Автоматизация теста к API Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики: Клиент создает заказ. Проверяется, что по треку заказа можно получить данные о заказе. Технические примечания: К проекту добавь файлы .gitignore и README.MD . Логи лежат в файле error.log в папке /var/www/backend/logs.

configuration.py URL_SERVICE = "https://111e81da-3545-40f4-b400-c5a9953f124f.serverhub.praktikum-services.ru/" CREATE_ORDER = "api/v1/orders" GET_ORDER = "/api/v1/orders/track"

data.py order_body = { "firstName": "Naruto", "lastName": "Uchiha", "address": "Konoha, 142 apt.", "metroStation": 4, "phone": "+7 800 355 35 35", "rentTime": 5, "deliveryDate": "2020-06-06", "comment": "Saske, come back to Konoha", "color": [ "BLACK" ] }

sender_stand_request.py import configuration import requests import data

def post_create_order(order_body) : return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=order_body) track_number = post_create_order(data.order_body).json()["track"]

response = post_create_order(data.order_body) print(response.status_code) print(response.json()["track"])

def get_order_on_number(): track = post_create_order(data.order_body).json()["track"] return requests.get(configuration.URL_SERVICE + configuration.REQUEST_ORDER + str(track))

response = get_order_on_number() print(response.status_code)

test_order_by_number.py import sender_stand_request def positive_assert(): order_response = sender_stand_request.get_order_on_number() assert order_response.status_code == 200

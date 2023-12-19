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

configuration.py
Файл `configuration.py` содержит определение переменных `URL_SERVICE`, `CREATE_ORDER` и `GET_ORDER`.

1. `URL_SERVICE` - переменная, используемая для хранения URL-адреса сервиса. Значение этой переменной является строкой `"https://111e81da-3545-40f4-b400-c5a9953f124f.serverhub.praktikum-services.ru/"`. 

2. `CREATE_ORDER` - переменная, используемая для хранения пути к API-методу создания заказа. Значение этой переменной является строкой `"api/v1/orders"`. 
3. `GET_ORDER` - переменная, используемая для хранения пути к API-методу получения информации о заказе. Значение этой переменной является строкой `"/api/v1/orders/track"`. 
URL_SERVICE = "https://111e81da-3545-40f4-b400-c5a9953f124f.serverhub.praktikum-services.ru/" CREATE_ORDER = "api/v1/orders" GET_ORDER = "/api/v1/orders/track"

data.py 
Данный фрагмент кода представляет собой инициализацию переменных headers и order_body.

Первая строка создает словарь headers, который содержит информацию о типе содержимого запроса. В данном случае, это application/json, что означает, что содержимое запроса представляет собой JSON-объект.

Вторая строка создает словарь order_body, который содержит информацию о заказе. Каждый ключ в словаре представляет отдельное поле заказа, а соответствующие значения - данные, связанные с этим полем. Например, "firstName" со значением "Semen" представляет имя заказчика, "lastName" со значением "Elokhin" - фамилию заказчика и так далее.

Таким образом, эта функция инициализирует переменные с информацией о заголовках запроса и теле заказа, которые могут использоваться для отправки запроса на сервер.
headers = {
    "Content-Type": "application/json"
}

order_body = {
    "firstName": "Semen",
    "lastName": "Elokhin",
    "address": "Lenina, 123",
    "metroStation": 5,
    "phone": "+7 925 555 55",
    "rentTime": 7,
    "deliveryDate": "2023-12-18",
    "comment": "Saske, come back to Lenina",
    "color": [
        "BLACK"
    ]
}

requests_function.py 
Этот файл содержит две функции для работы с внешним сервисом через библиотеку requests.

Функция post_new_order() выполняет HTTP POST запрос к сервису, чтобы создать новый заказ. Она использует модули configuration и data для получения необходимых данных. Внутри функции выполняется запрос с помощью requests.post() метода, передавая URL сервиса и путь к созданию заказа, а также данные заказа и заголовки, которые хранятся в модуле data.

Функция get_order(track_number) выполняет HTTP GET запрос к сервису для получения информации о заказе по его номеру. Она также использует модули configuration и data для получения данных. Внутри функции происходит запрос с помощью requests.get() метода, передавая URL сервиса и путь к получению заказа, а также параметр track_number, который содержит номер заказа.

Обе функции выполняют запросы к внешнему сервису и возвращают ответы от сервера. Они используют модули configuration и data для получения URL сервиса, путей к различным эндпоинтам и других необходимых данных.
import requests
import configuration
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body,
                         headers=data.headers)


def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params={"t": track_number})

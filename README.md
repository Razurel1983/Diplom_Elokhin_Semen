# Diplom_Elokhin_Semen

В проекте представлены:

SQL-запросы для получения данных из БД Яндекс Самокат; Автотест к API; Скриншот с запуском теста в PyCharm.

Информация по запуску тестов: Для запуска тестов должны быть установлены пакеты pytest и requests Запуск всех тестов выполянется командой pytest

SQL запросы Задание 1 Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных. Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).
SELECT "Couriers".login,
COUNT(*)
FROM "Couriers"
LEFT JOIN "Orders" ON "Couriers".id = "Orders"."courierId"
WHERE "Orders"."inDelivery" = true
GROUP BY "Couriers".login;
Ссылка на скриншот выполненого запроса: https://drive.google.com/file/d/1Sd7fUcTY55PixA6Igjit86mhCHBAVVP_/view?usp=sharing


Задание 2 Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно. Для этого: выведи все трекеры заказов и их статусы.

Ссылка на скриншот выполненого запроса: https://drive.google.com/file/d/16g9Y0cXFiAh9PAo6uIy94p95OxsO8rcc/view?usp=sharing

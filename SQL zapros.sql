-- noinspection SqlNoDataSourceInspectionForFile
Задание 1
SELECT "Couriers".login,
COUNT(*)
FROM "Couriers"
LEFT JOIN "Orders" ON "Couriers".id = "Orders"."courierId"
WHERE "Orders"."inDelivery" = true
GROUP BY "Couriers".login;


Задание 2
SELECT track,
   CASE
          WHEN finished=true THEN 2
          WHEN cancelled=true THEN -1
          WHEN "inDelivery"=true THEN 1
      ELSE 0
      END as status_zakaza
 FROM "Orders";
### Задание 1

Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных. Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

### Решение

```sql
SELECT c.login, COUNT(o."courierId")
    FROM "Couriers" AS c 
    INNER JOIN "Orders" AS o ON c.id = o."courierId" 
    WHERE "inDelivery" = true 
    GROUP BY c.login;
```
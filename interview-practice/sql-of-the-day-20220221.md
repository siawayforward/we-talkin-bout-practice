# Average Order Value

This question was asked by: **Klaviyo**

Given three tables, representing customer transactions and customer attributes:

Write a query to get the average order value by gender.

Note: We’re looking at the average order value by users that have ever placed an order. Additionally, please round your answer to two decimal places.

## Example

### Input

#### transactions table

|Column|Type|
|------|----|
|id|INTEGER|
|user_id|INTEGER|
|created_at|DATETIME|
|product_id|INTEGER|
|quantity|INTEGER|

#### users table

|Column|Type|
|------|----|
|id|INTEGER|
|name|VARCHAR|
|sex|VARCHAR|

#### products table

|Column|Type|
|------|----|
|id|INTEGER|
|name|VARCHAR|
|price|FLOAT|

### Output

|Column|Type|
|------|----|
|sex|VARCHAR|
|aov|FLOAT|

### My Solution

So I overthought this question. To note, you get the same answer, but I started here.

```sql
SELECT sex
, CAST(order_value AS DECIMAL)/customers AS aov
FROM
(
    SELECT u.sex
    , SUM(p.price * t.quantity) AS order_value
    , COUNT(t.user_id) AS customers
    FROM transactions t
    LEFT JOIN users u ON u.id = u.user_id
    LEFT JOIN products p ON p.id = t.product_id
    WHERE u.id IS NOT NULL -- only those with transactions
    GROUP BY 1
) orders_by_sex
GROUP BY 1
ORDER BY 1,2
;
```

After looking at the question again, I was like Sia this is too much, so ended up here

```sql
SELECT u.sex
, AVG(p.price * t.quantity) AS order_value
FROM transactions t
INNER JOIN users u ON u.id = t.user_id
INNER JOIN products p ON p.id = t.product_id
GROUP BY 1
;
```

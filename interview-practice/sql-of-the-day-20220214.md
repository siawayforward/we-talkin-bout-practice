# Popular Apple Actions

This question was asked by: **Hulu**

Write a query to determine the top 5 actions performed during the month of November 2020, for actions performed on an Apple platform (iPhone, iPad).

The `events` table tracks every time a user performs a certain action (like post_enter, etc.) on a platform (android, web, etc.).

The output should include the action performed and it’s rank in ascending order. If two actions are performed equally, they should have the same rank.

## Example

### Input

#### events table

| Column | Type|
| -------|-----|
| user_id|INTEGER|
| created_at|DATETIME|
| action|VARCHAR|
| platform | VARCHAR |

### Output

| Column| Type|
| ------|-------|
| action| VARCHAR|
| ranks| INTEGER |

### My Solution

```sql
SELECT action
, RANK() OVER(PARTITION BY action ORDER BY action_ct DESC) AS rank
FROM
(
    SELECT action
    , COUNT(user_id) as action_ct
    FROM events 
    WHERE platform IN ('iPhone','iPad')
    AND MONTH(created_at) = 11 AND YEAR(created_at) = 2020
    GROUP BY 1
) a
GROUP BY 1
HAVING rank <= 5
;
```

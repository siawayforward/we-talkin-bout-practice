# Employee Salaries

Given a `employees` and `departments` table, select the top 3 departments with at least ten employees and rank them according to the percentage of their employees making over 100K in salary.

## Example

### Input

employees table

|| Columns || Type ||
| id | INTEGER |
| first_name | VARCHAR |
| last_name | VARCHAR |
| salary | INTEGER |
| department_id | INTEGER |

departments table

|| Columns || Type ||
| id | INTEGER |
| name | VARCHAR |

### Output

|| Columns || Type ||
| percentage_over_100K | FLOAT |
| department_name | VARCHAR |
| number of employees | INTEGER |

#### My Solution

```sql
WITH department_metrics AS
(
    SELECT d.name
    , COUNT(e.id) AS total_emp
    , SUM(CASE WHEN e.salary > 100000 THEN 1 ELSE 0 END) AS over_100K_emp
    FROM employee e 
    LEFT JOIN departments d ON d.id = e.department_id
    GROUP BY 1
    HAVING COUNT(e.id) >= 10
    ORDER BY 2 DESC 
)
SELECT over_100K_emp*100/total_emp AS percentage_over_100K
, name AS department_name
, total_emp AS number_of_employees
FROM department_metrics
GROUP BY 2,3
ORDER BY 1 DESC
LIMIT 3; 
```

# Write your MySQL query statement below
WITH Filtered AS (
    SELECT id, visit_date, people
    FROM Stadium
    WHERE people >= 100
),
Numbered AS (
    SELECT 
        id, 
        visit_date, 
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Filtered
),
GroupedCounts AS (
    SELECT *,
           COUNT(*) OVER (PARTITION BY grp) AS cnt
    FROM Numbered
)
SELECT id, visit_date, people
FROM GroupedCounts
WHERE cnt >= 3
ORDER BY visit_date ASC;
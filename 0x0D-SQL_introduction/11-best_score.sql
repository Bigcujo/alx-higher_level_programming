-- lists all the names with a scroe >=10.
-- the records will be printed in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;

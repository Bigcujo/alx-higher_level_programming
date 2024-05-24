-- this list number of records with the same score in the second table.
-- this will be ordered in descending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;

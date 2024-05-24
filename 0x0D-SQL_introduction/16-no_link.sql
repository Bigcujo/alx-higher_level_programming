-- this lists all records of the with a name value.
-- the records will be printed in descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;

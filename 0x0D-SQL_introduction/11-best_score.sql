-- lists all records with in the table second_table in my MySQL server.
-- where a score >= 10 and ordered descendingly.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;

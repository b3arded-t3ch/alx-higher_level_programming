-- lists all records of second_table in my MySQL server.
-- Doesn’t list rows without a name value
-- Results displays the score and the name (in this order)
-- Records listed by descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;

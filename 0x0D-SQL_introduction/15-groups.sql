-- List the number of records wiht the same score in the table second_table.
-- Records are ordered by descending count.
SELECT `score` COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;

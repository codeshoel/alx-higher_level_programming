-- List all records of the table second_table.
-- Records are listed and ordered by desc score
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;

-- Displays the average temprature (in Fahrenheit)
-- ordered by city by desc temprature.
SELECT `city`, AVG() AS `avg_temp`
FROM `temperature`
GROUP BY `city`
ORDER BY `avg_temp` DESC;

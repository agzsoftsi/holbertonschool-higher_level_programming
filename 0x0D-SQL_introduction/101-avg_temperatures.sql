-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Import in hbtn_0c_0 database this table dump - IMPORT TABLE FROM
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;

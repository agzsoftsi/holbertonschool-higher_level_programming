-- Displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- Import in hbtn_0c_0 database this table dump - same of 101 task
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;

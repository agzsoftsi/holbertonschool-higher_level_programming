-- Displays the max temperature of each state (ordered by State name)
-- Import in hbtn_0c_0 database this table dump - same of task 101
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;

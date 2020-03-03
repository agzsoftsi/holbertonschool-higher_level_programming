-- List all cities in the database hbtn_0d_usa
-- cities.id - cities.name - states.name, sorted in ascending order by cities.id, only one SELECT statement
SELECT cities.id, cities.name, states.name FROM states RIGHT JOIN cities ON cities.state_id = states.id;

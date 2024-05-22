-- Lists all cities in database hbtn_0d_usa
-- Use one SELECT element.
SELECT cities.id, cities.name, states.name,
FROM cities
LEFT JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

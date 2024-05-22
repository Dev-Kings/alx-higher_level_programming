-- Lists all cities in database hbtn_0d_usa
-- Use one SELECT element.
SELECT cities.id, cities.name, states.name,
FROM cities
INNER JOIN states ON cities.state_id = state.id
ORDER BY cities.id ASC;

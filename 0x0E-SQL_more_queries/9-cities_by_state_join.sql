-- Lists all cities in database hbtn_0d_usa
-- Use one SELECT element.
SELECT cities.id AS id,
cities.name AS name,
states.name AS name,
FROM cities
JOIN states ON cities.state_id = state.id
ORDER BY cities.id ASC;

-- Lists all cities in database hbtn_0d_usa
-- Use one SELECT element.
SELECT cities.id, cities.name, states.name,
FROM cities
LEFT JOIN states ON states.id = cities.id
ORDER BY cities.id ASC;

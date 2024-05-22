-- Lists all cities California on database hbtn_0d_usa
-- Only cities of California state.
SELECT id, name FROM cities
WHERE cities.state_id IN (
	SELECT id FROM states WHERE name = "California"
ORDER BY id ASC
);

-- Lists all cities California on database hbtn_0d_usa
-- Only cities of California state.
SELECT * FROM cities
WHERE cities.state_id = (
	SELECT id FROM states WHERE name = "California"
);

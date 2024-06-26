-- Creates database hbtn_0d_usa and table cities in the database
-- cities id integer, unique not null and must be a foregin key
-- referencing id of states table
-- name is variable character length of maximum 256 and not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `cities` (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(`id`),
	FOREIGN KEY(`state_id`) REFERENCES states(`id`)
	);

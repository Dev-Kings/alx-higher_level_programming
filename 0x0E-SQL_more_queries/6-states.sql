-- creates database hbtn_0d_usa and table states
-- In the database hbtn_0d_usa
-- id unique, auto incremented, not null, primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS `states` (
	id INT NOT NULL UNIQUE AUTO INCREMENT PRIMARY KEY,
	name VARCHAR(256),
	);

-- Creates table unique_id
-- id with default value 1 and must be unique
-- name variable character max length 256
CREATE TABLE IF NOT EXISTS `unique_id`(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);

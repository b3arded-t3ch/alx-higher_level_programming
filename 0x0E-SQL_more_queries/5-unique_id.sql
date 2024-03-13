-- This script creates the table unique_id on my MySQL server.
CREATE TABLE IF NOT EXISTS unique_id(
	`id` INT DEFAULT 1 PRIMARY KEY,
	`name` VARCHAR(256)
	);

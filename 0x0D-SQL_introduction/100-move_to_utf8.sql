-- Converts hbtn_0c_0 database to utf8mb4
-- and collate utf8mb4_unicode_ci
USE hbtn_0c_0
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

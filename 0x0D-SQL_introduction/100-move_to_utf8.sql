-- Convert the database hbtn_0c_0 to UTF8 in MYSQL server.
USE `hbtn_0c_0`
ALERT TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

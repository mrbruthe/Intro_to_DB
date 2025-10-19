-- task_3.sql
-- Lists all tables in the given database (alx_book_store)
-- without using SHOW or SELECT *

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = DATABASE();

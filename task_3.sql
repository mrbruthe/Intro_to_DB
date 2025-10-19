-- task_3.sql
-- This script lists all tables in the alx_book_store database

USE alx_book_store;

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_SCHEMA = 'alx_book_store';

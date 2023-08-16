-- A script that lists all the tables of a database.
USE information_schema;

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'information_schema';

-- A script that prints the full description of the table first_table from the database hbtn_0c_0
SELECT GROUP_CONCAT(
    CONCAT(column_name, ' ', column_type, ' ', IF(is_nullable = 'NO', 'NOT NULL', ''), ' ',
           IF(column_default IS NOT NULL, CONCAT('DEFAULT ', column_default), ''))
    SEPARATOR ',\n  '
) AS create_table
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0'
    AND table_name = 'first_table';

-- this script prints the full decription of the table  creted.
SELECT
    COLUMN_NAME AS 'Column Name',
    COLUMN_TYPE AS 'Column Type',
    IS_NULLABLE AS 'Is Nullable',
    COLUMN_KEY AS 'Key',
    COLUMN_DEFAULT AS 'Default',
    EXTRA AS 'Extra'
FROM
    information_schema.COLUMNS
WHERE
    TABLE_SCHEMA = DATABASE() AND
    TABLE_NAME = 'first_table';

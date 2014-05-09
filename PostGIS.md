PostGIS
=======

Queries
-------

```sql
-- Create an unique id
SELECT ROW_NUMBER() OVER (ORDER BY name) AS id
FROM table;

-- Create a line between two points
SELECT ST_MakeLine(a.geom, b.geom) :: Geometry(LineString, 21781) AS geom
FROM table1 a
JOIN table2 b ON a.id = b.fk;

-- Set first character to uppercase
SELECT ((UPPER(SUBSTR(street, 1, 1)) || SUBSTR(street, 2))) :: varchar AS street
FROM table;

-- Replace all the text before a specific character
SELECT REGEXP_REPLACE(place, '^[^, ]*, ', '') AS place
FROM table;

-- Test if a value is an integer
SELECT
    CASE
        WHEN value ~ '^[0-9]+$' THEN TRUE
        ELSE FALSE
    END
    AS is_integer
FROM table;

-- Concatenate strings with possible null values
SELECT street || ' ' || num || COALESCE(suffix, '') AS address
FROM addresses;
```

Sequences
---------

```sql
-- Set current value
SELECT setval('schema.table_field_seq', 1000);
```

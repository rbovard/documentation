PostGIS
=======

Queries
-------

```sql
-- Create an unique id
SELECT ROW_NUMBER() OVER (ORDER BY name) AS id
FROM table;

-- Set first character to uppercase
SELECT ((UPPER(SUBSTR(street, 1, 1)) || SUBSTR(street, 2))) :: varchar AS street
FROM table;

-- Replace all the text before a specific character
SELECT REGEXP_REPLACE(place, '^[^, ]*, ', '') AS place
FROM table;

-- Erase a string if found
SELECT
    CASE
        WHEN value ~ '.* PN .*' THEN REGEXP_REPLACE(value, ' (PN...)', '')
        ELSE value
    END
    AS value
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

-- Split values into rows
SELECT id, regexp_split_to_table(no_parcelle, ';') AS no_parcelle
FROM table;
```

Spatial queries
---------------

```sql
-- Create a line between two points
SELECT ST_MakeLine(a.geom, b.geom) :: Geometry(LineString, 21781) AS geom
FROM table1 a
JOIN table2 b ON a.id = b.fk;

-- Return intersected features
SELECT ST_Intersection(a.geom, b.geom) AS geom
FROM table1 a, table2 b
WHERE ST_Intersects(a.geom, b.geom);

-- Merge polygons with an attribute
SELECT attribute, ST_Union(ST_SnapToGrid(geom, 0.0001)) :: Geometry(MultiPolygon, 21781) AS geom
FROM table
GROUP BY attribute;
```

Triggers
--------

```sql
-- Get parcel number
BEGIN
    SELECT INTO new.no_parcelle numero
    FROM mo.mo_par
    WHERE ST_Within(new.geom, geom);
    RETURN new;
END;

-- Get parcels numbers
BEGIN
    SELECT INTO new.no_parcelle String_Agg(numero, ';' ORDER BY numero)
    FROM mo.mo_par
    WHERE ST_Intersects(ST_Buffer(new.geom, -0.1), geom)
    GROUP BY new.fid;
    RETURN new;
END;
```

Sequences
---------

```sql
-- Set current value
SELECT setval('schema.table_field_seq', 1000);
```

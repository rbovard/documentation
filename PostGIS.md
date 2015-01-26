PostGIS
=======

Data types
----------

| Type          | Name                                  |
| ------------- | ------------------------------------- |
| **Character** | `varchar(255)`, `varchar(50)`, `text` |
| **Numeric**   | `int4`, `float8`                      |
| **Boolean**   | `bool`                                |
| **Date/Time** | `date`, `timestamp`                   |

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
SELECT id, REGEXP_SPLIT_TO_TABLE(no_parcelle, ';') AS no_parcelle
FROM table;

-- Add an unit to a value
SELECT (ROUND(length :: numeric, 2) || ' m') :: varchar AS length
FROM table;

-- Convert numeric to string
SELECT
    TRIM(TO_CHAR(p.numero :: numeric, '9999 999 9')) :: varchar(20) AS numero,
    TRIM(TO_CHAR(ST_X(p.geom), '999G999.99 m')) :: varchar(20) AS coord_y,
    TRIM(TO_CHAR(ST_Y(p.geom), '999G999.99 m')) :: varchar(20) AS coord_x,
    TRIM(TO_CHAR(p.geomalt, '9G999.99 m')) :: varchar(20) AS altitude
FROM mo.mo_pfp1 p;
```

Spatial queries
---------------

```sql
-- Spatial join (point in polygon)
SELECT *
FROM table1 a, table2 b
WHERE ST_Within(a.geom, b.geom);

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

-- Check validity of geometries
SELECT *
FROM table
WHERE ST_IsValid(geom) = true;

-- Return features inside buffer around points
SELECT a.*
FROM table1 a
JOIN table2 b ON ST_Contains(ST_Buffer(b.geom, 100), a.geom);

-- Order results by list
SELECT *
FROM osm.osm_roads r
ORDER BY
    CASE
        WHEN r.highway IN ('motorway', 'motorway_link') THEN 1
        WHEN r.highway = 'primary' THEN 2
        WHEN r.highway = 'secondary' THEN 3
        WHEN r.highway = 'tertiary' THEN 4
        ELSE 5
    END DESC;
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

-- Get absolute path
BEGIN
    SELECT INTO new.file
    CASE
        WHEN new.file IS NOT NULL THEN replace(new.file, 'X:\', '\\path\to\folder\')
        ELSE NULL
    END;
    RETURN new;
END;
```

Sequences
---------

```sql
-- Set current value
SELECT setval('schema.table_field_seq', 1000);
```

Geometries
----------

```sql
-- Create column
SELECT AddGeometryColumn(
    'schema', 'table',
    'geom', 21781,
    'Point|MultiLineString|MultiPolygon', 2
);

-- Create index
CREATE INDEX table_geom_idx
ON schema.table
USING gist (geom);
```

Information schema
------------------

```sql
-- Get all tables
SELECT table_schema, table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
AND table_schema <> 'information_schema'
AND table_schema <> 'public'
AND table_schema <> 'pg_catalog'
ORDER BY table_schema, table_name;
```

Miscellaneous
-------------

```sql
-- Get PostGIS version
SELECT PostGIS_full_version();
```

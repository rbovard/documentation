PostGIS
=======

* [Create table](#create-table)
    * [Create index](#create-index)
* [Data types](#data-types)
* [Geometries](#geometries)
    * [Activate PostGIS extension](#activate-postgis-extension)
    * [Create column](#create-column)
    * [Create spatial index](#create-spatial-index)
    * [Convert simple geometry to multi geometry](#convert-simple-geometry-to-multi-geometry)
    * [Convert MultiPoint to Point](#convert-multipoint-to-point)
    * [Change projection](#change-projection)
    * [Create polygon with closed linestrings](#create-polygon-with-closed-linestrings)
* [Queries](#queries)
    * [Create an unique id](#create-an-unique-id)
    * [Set first character to uppercase](#set-first-character-to-uppercase)
    * [Replace all the text before a specific character](#replace-all-the-text-before-a-specific-character)
    * [Erase a string if found](#erase-a-string-if-found)
    * [Test if a value is an integer](#test-if-a-value-is-an-integer)
    * [Convert booleans to strings](#convert-booleans-to-strings)
    * [Concatenate strings with possible null values](#concatenate-strings-with-possible-null-values)
    * [Split values into rows](#split-values-into-rows)
    * [Add an unit to a value](#add-an-unit-to-a-value)
    * [Convert numeric to string](#convert-numeric-to-string)
    * [Convert date to string](#convert-date-to-string)
    * [Order results by list](#order-results-by-list)
    * [Split string with a separator and get specific part](#split-string-with-a-separator-and-get-specific-part)
* [Spatial queries](#spatial-queries)
    * [Spatial join (point in polygon)](#spatial-join-point-in-polygon)
    * [Create a line between two points](#create-a-line-between-two-points)
    * [Return intersected features](#return-intersected-features)
    * [Merge polygons with an attribute](#merge-polygons-with-an-attribute)
    * [Check validity of geometries](#check-validity-of-geometries)
    * [Return features inside buffer around points](#return-features-inside-buffer-around-points)
    * [Create a parallel](#create-a-parallel)
    * [Create a zone with buffers](#create-a-zone-with-buffers)
    * [Return the nth point of a linestring](#return-the-nth-point-of-a-linestring)
    * [Get azimuth of a linestring](#get-azimuth-of-a-linestring)
    * [Extract boundary of a MultiPolygon into a MultiLineString](#extract-boundary-of-a-multipolygon-into-a-multilinestring)
* [Triggers](#triggers)
    * [Get parcel number](#get-parcel-number)
    * [Get parcels numbers](#get-parcels-numbers)
    * [Get absolute path](#get-absolute-path)
* [Sequences](#sequences)
    * [Set current value](#set-current-value)
* [Constraints](#constraints)
    * [Drop foreign key only if exists](#drop-foreign-key-only-if-exists)
* [Information schema](#information-schema)
    * [Get all tables](#get-all-tables)
    * [Get all views](#get-all-views)
    * [Get all triggers](#get-all-triggers)
    * [Get all sequences](#get-all-sequences)
    * [Get tables with wrong SRID](#get-tables-with-wrong-srid)
    * [Get tables with wrong geometry type](#get-tables-with-wrong-geometry-type)
* [Miscellaneous](#miscellaneous)
    * [Get PostGIS version](#get-postgis-version)
    * [Set schema](#set-schema)
* [psql](#psql)
    * [Create database with template](#create-database-with-template)
    * [Create schema and allow rights](#create-schema-and-allow-rights)
    * [Dump and restore database](#dump-and-restore-database)
* [Backup and restore](#backup-and-restore)
    * [Backup in custom format](#backup-in-custom-format)
    * [Backup specific schemas](#backup-specific-schemas)
    * [Restore backup](#restore-backup)
* [Log Analyzer](#log-analyzer)
    * [pgBadger](#pgbadger)

Create table
------------

```sql
CREATE TABLE <schema>.<table> (id serial PRIMARY KEY);
COMMENT ON TABLE <schema>.<table> IS '<comment>';
```

### Create index

```sql
CREATE INDEX <table>_<field>_idx
ON <schema>.<table>
USING btree (<field>);
```

Data types
----------

| Type          | Name                                       |
| ------------- | ------------------------------------------ |
| **Character** | `varchar(255)`, `varchar(50)`, `text`      |
| **Numeric**   | `int4`, `float8`                           |
| **Boolean**   | `bool`                                     |
| **Date/Time** | `date`, `timestamp`                        |
| **Geometry**  | `Point`, `MultiLineString`, `MultiPolygon` |

Geometries
----------

### Activate PostGIS extension

```sql
CREATE EXTENSION postgis;
```

### Create column

```sql
ALTER TABLE <schema>.<table> ADD COLUMN geom geometry(<Point|MultiLineString|MultiPolygon>, 21781);
```

### Create spatial index

```sql
CREATE INDEX <table>_geom_idx
ON <schema>.<table>
USING gist (geom);
```

### Convert simple geometry to multi geometry

```sql
SELECT ST_Multi(geom) :: Geometry(<MultiLineString|MultiPolygon>, 21781) AS geom
FROM <table>;
```

See [convert_simple_geometry_to_multi.sql](../sql/convert_simple_geometry_to_multi.sql)

### Convert MultiPoint to Point

```sql
SELECT (ST_Dump(geom)).geom :: Geometry(Point, 21781) AS geom
FROM <table>;
```

### Change projection

```sql
SELECT ST_Transform(geom, 21781) :: Geometry(<Point|MultiLineString|MultiPolygon>, 21781) AS geom
FROM <table>;
```

### Create polygon with closed linestrings

```sql
SELECT ST_MakePolygon((ST_Dump(geom)).geom) AS geom
FROM <table>
WHERE ST_IsClosed(geom);
```

Queries
-------

### Create an unique id

```sql
SELECT ROW_NUMBER() OVER (ORDER BY <column>) AS id
FROM <table>;
```

### Set first character to uppercase

```sql
SELECT ((UPPER(SUBSTR(<column>, 1, 1)) || SUBSTR(<column>, 2))) :: varchar AS <column>
FROM <table>;
```

### Replace all the text before a specific character

```sql
SELECT REGEXP_REPLACE(<column>, '^[^<char> ]*<char> ', '') AS <column>
FROM <table>;
```

### Erase a string if found

```sql
SELECT
    CASE
        WHEN <column> ~ '.* <string> .*' THEN REGEXP_REPLACE(<column>, ' <new-string> ', '')
        ELSE <column>
    END
    AS <column>
FROM <table>;
```

### Test if a value is an integer

```sql
SELECT
    CASE
        WHEN <column> ~ '^[0-9]+$' THEN TRUE
        ELSE FALSE
    END
    AS is_integer
FROM <table>;
```

### Convert booleans to strings

```sql
SELECT
    CASE <column>
        WHEN TRUE THEN 'Yes'
        WHEN FALSE THEN 'No'
        ELSE NULL
    END
    AS yes_no
FROM <table>;
```

### Concatenate strings with possible null values

```sql
SELECT street || ' ' || num || COALESCE(suffix, '') AS address
FROM addresses;
```

### Split values into rows

```sql
SELECT id, REGEXP_SPLIT_TO_TABLE(no_parcelle, ';') AS no_parcelle
FROM <table>;
```

### Add an unit to a value

```sql
SELECT (ROUND(length :: numeric, 2) || ' m') :: varchar AS length
FROM <table>;
```

### Convert numeric to string

```sql
SELECT
    TRIM(TO_CHAR(p.numero :: numeric, '9999 999 9')) :: varchar(20) AS numero,
    TRIM(TO_CHAR(ST_X(p.geom), '999G999.99 m')) :: varchar(20) AS coord_y,
    TRIM(TO_CHAR(ST_Y(p.geom), '999G999.99 m')) :: varchar(20) AS coord_x,
    TRIM(TO_CHAR(p.geomalt, '9G999.99 m')) :: varchar(20) AS altitude
FROM mo.mo_pfp1 p;
```

### Convert date to string

```sql
SELECT to_char(<column>, 'DD.MM.YYYY') AS <column>
FROM <table>;
```

### Order results by list

```sql
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

### Split string with a separator and get specific part

```sql
SELECT (REGEXP_SPLIT_TO_ARRAY(<attribute>, '/'))[3] AS <column>
FROM <table>;
```

Spatial queries
---------------

### Spatial join (point in polygon)

```sql
SELECT *
FROM <table1> a, <table2> b
WHERE ST_Within(a.geom, b.geom);
```

### Create a line between two points

```sql
SELECT ST_MakeLine(a.geom, b.geom) :: Geometry(LineString, 21781) AS geom
FROM <table1> a
JOIN <table2> b ON a.id = b.fk;
```

### Return intersected features

```sql
SELECT ST_Intersection(a.geom, b.geom) AS geom
FROM <table1> a, <table2> b
WHERE ST_Intersects(a.geom, b.geom);
```

### Merge polygons with an attribute

```sql
SELECT attribute, ST_Union(ST_SnapToGrid(geom, 0.0001)) :: Geometry(MultiPolygon, 21781) AS geom
FROM <table>
GROUP BY attribute;
```

### Check validity of geometries

```sql
SELECT *
FROM <table>
WHERE ST_IsValid(geom) = true;
```

### Return features inside buffer around points

```sql
SELECT a.*
FROM <table1> a
JOIN <table2> b ON ST_Contains(ST_Buffer(b.geom, 100), a.geom);
```

### Create a parallel

```sql
SELECT ST_OffsetCurve((ST_Dump(geom)).geom :: Geometry(LineString, 21781), <offset>) :: Geometry(MultiLineString, 21781) AS geom
FROM <table>;
```

### Create a zone with buffers

```sql
SELECT ST_Multi(ST_Union(ST_SnapToGrid(ST_Buffer(geom, <radius>), 0.0001))) :: Geometry(MultiPolygon, 21781) AS geom
FROM <table>;
```

### Return the nth point of a linestring

```sql
SELECT ST_PointN(geom, <n>) AS geom
FROM <table>;
```

### Get azimuth of a linestring

```sql
WITH line AS (
    SELECT
        ST_PointN((ST_Dump(geom)).geom, 1) :: Geometry(Point, 21781) as p1,
        ST_PointN((ST_Dump(geom)).geom, 2) :: Geometry(Point, 21781) as p2
    FROM <table>
)
SELECT
    degrees(ST_Azimuth(p1, p2)) AS azimuth
FROM line;
```

### Extract boundary of a MultiPolygon into a MultiLineString

```sql
SELECT ST_Boundary(geom) AS geom
FROM <table>
```

Triggers
--------

### Get parcel number

```sql
BEGIN
    SELECT INTO new.no_parcelle numero
    FROM mo.mo_par
    WHERE ST_Within(new.geom, geom);
    RETURN new;
END;
```

### Get parcels numbers

```sql
BEGIN
    SELECT INTO new.no_parcelle String_Agg(numero, ';' ORDER BY numero)
    FROM mo.mo_par
    WHERE ST_Intersects(ST_Buffer(new.geom, -0.1), geom)
    GROUP BY new.fid;
    RETURN new;
END;
```

### Get absolute path

```sql
BEGIN
    SELECT INTO new.file
    CASE
        WHEN new.file IS NOT NULL THEN replace(new.file, '<drive>', '<absolute-path>') --'X:', '\\path\to\folder'
        ELSE NULL
    END;
    RETURN new;
END;
```

Sequences
---------

### Set current value

```sql
SELECT setval('<schema>.<table>_<field>_seq', (SELECT MAX(<field>) FROM <schema>.<table>));
```

Constraints
-----------

### Drop foreign key only if exists

```sql
ALTER TABLE <schema>.<table> DROP CONSTRAINT IF EXISTS <table>_<field>_fkey;
```

Information schema
------------------

### Get all tables

```sql
SELECT t.table_schema, t.table_name
FROM information_schema.tables t
WHERE t.table_type = 'BASE TABLE'
AND t.table_schema NOT IN ('information_schema', 'pg_catalog', 'public', 'topology')
ORDER BY t.table_schema, t.table_name;
```

#### With type (slow query)

```sql
SELECT t.table_schema, t.table_name,
    CASE
        WHEN g.type IS NOT NULL THEN g.type
        ELSE 'TABLE'
    END AS table_type
FROM information_schema.tables t
LEFT JOIN geometry_columns g ON g.f_table_schema || '.' || g.f_table_name = t.table_schema || '.' || t.table_name
WHERE t.table_type = 'BASE TABLE'
AND t.table_schema NOT IN ('information_schema', 'pg_catalog', 'public', 'topology')
ORDER BY t.table_schema, t.table_name;
```

#### Only with geometry

```sql
SELECT t.table_schema, t.table_name, g.type
FROM information_schema.tables t
JOIN geometry_columns g ON g.f_table_schema || '.' || g.f_table_name = t.table_schema || '.' || t.table_name
WHERE t.table_type = 'BASE TABLE'
AND t.table_schema NOT IN ('information_schema', 'pg_catalog', 'public', 'topology')
ORDER BY t.table_schema, t.table_name;
```

### Get all views

```sql
SELECT v.table_schema, v.table_name, v.view_definition
FROM information_schema.views v
WHERE v.table_schema NOT IN ('information_schema', 'pg_catalog', 'public', 'topology')
ORDER BY v.table_schema, v.table_name;
```

### Get all triggers

```sql
SELECT r.routine_schema, r.routine_name, r.routine_definition
FROM information_schema.routines r
WHERE r.routine_definition LIKE 'BEGIN%'
ORDER BY r.routine_schema, r.routine_name;
```

### Get all sequences

```sql
SELECT c.relname
FROM pg_class c
WHERE c.relkind = 'S'
ORDER BY c.relname;
```

### Get tables with wrong SRID

```sql
SELECT g.f_table_catalog, g.f_table_schema, g.f_table_name, g.f_geometry_column, g.coord_dimension, g.srid, g.type
FROM geometry_columns g
WHERE g.srid <> 21781
ORDER BY g.f_table_schema, g.f_table_name;
```

### Get tables with wrong geometry type

```sql
SELECT g.f_table_catalog, g.f_table_schema, g.f_table_name, g.f_geometry_column, g.coord_dimension, g.srid, g.type
FROM geometry_columns g
WHERE g.type NOT IN ('POINT', 'MULTILINESTRING', 'MULTIPOLYGON')
ORDER BY g.f_table_schema, g.f_table_name;
```

Miscellaneous
-------------

### Get PostGIS version

```sql
SELECT PostGIS_full_version();
```

### Set schema

```bash
SET search_path = <schema>;
```

psql
----

### Create database with template

```bash
sudo -u postgres createdb --template=template_postgis <database>
```

### Create schema and allow rights

```bash
sudo -u postgres psql -c 'CREATE SCHEMA <schema>' <database>
sudo -u postgres psql -c 'GRANT ALL ON SCHEMA <schema> TO "<user>"' <database>
```

### Dump and restore database

```bash
sudo -u postgres pg_dump <source_database> > <source_database>.sql
sudo -u postgres dropdb <target_database>
sudo -u postgres createdb <target_database>
sudo -u postgres psql -d <target_database> -f <source_database>.sql
```

Backup and restore
------------------

### Backup in custom format

```bash
pg_dump --format=custom --blobs <database> --file=<database>.backup
```

### Backup specific schemas

```bash
pg_dump --format=custom --blobs <database> --schema='<pattern>' --file=<database>.backup
```

### Restore backup

```bash
pg_restore --dbname=<database> <database>.backup
```

Log
---

### pgBadger

```bash
cd /d <path-to-postgres-data>\pg_log
dir postgresql-<YYYY-MM>-* /b > list-<YYYY-MM>.txt
perl "<path-to-pgbadger>\pgbadger" --exclude-time "^* (20|21|22|23):*" --exclude-query="^(COPY|COMMIT|FETCH|VACUUM)" --disable-checkpoint --disable-lock --disable-temporary --disable-autovacuum --outfile postgresql-<YYYY-MM>.html --logfile-list list-<YYYY-MM>.txt
del list-<YYYY-MM>.txt
```

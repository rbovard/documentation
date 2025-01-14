# PostGIS

* [Tables](#tables)
    * [Create table](#create-table)
    * [Create table from a query](#create-table-from-a-query)
    * [Create index](#create-index)
    * [Change table schema](#change-table-schema)
* [Data types](#data-types)
    * [Create UUID field](#create-uuid-field)
    * [Convert integer to UUID](#convert-integer-to-uuid)
* [Geometries](#geometries)
    * [Activate PostGIS extension](#activate-postgis-extension)
    * [Create column](#create-column)
    * [Insert geometry from text](#insert-geometry-from-text)
    * [Create spatial index](#create-spatial-index)
    * [Convert simple geometry to multi geometry](#convert-simple-geometry-to-multi-geometry)
    * [Convert MultiPoint to Point](#convert-multipoint-to-point)
    * [Change projection](#change-projection)
    * [Set table geometry and projection](#set-table-geometry-and-projection)
    * [Create polygon with closed linestrings](#create-polygon-with-closed-linestrings)
* [Queries](#queries)
    * [Create an unique id](#create-an-unique-id)
    * [Set first character to uppercase](#set-first-character-to-uppercase)
    * [Change text to uppercase](#change-text-to-uppercase)
    * [Replace all the text before a specific character](#replace-all-the-text-before-a-specific-character)
    * [Erase a string if found](#erase-a-string-if-found)
    * [Test if a value is an integer](#test-if-a-value-is-an-integer)
    * [Convert booleans to strings](#convert-booleans-to-strings)
    * [Concatenate strings with possible null values](#concatenate-strings-with-possible-null-values)
    * [Concatenate strings in an aggregate expression](#concatenate-strings-in-an-aggregate-expression)
    * [Split values into rows](#split-values-into-rows)
    * [Add an unit to a value](#add-an-unit-to-a-value)
    * [Convert numeric to string](#convert-numeric-to-string)
    * [Convert date to string](#convert-date-to-string)
    * [Convert string to date](#convert-string-to-date)
    * [Get previous business day](#get-previous-business-day)
    * [Get next business day](#get-next-business-day)
    * [Sort results by list](#sort-results-by-list)
    * [Sort results by varchar as numeric](#sort-results-by-varchar-as-numeric)
    * [Sort results by descending order with null at the end](#sort-results-by-descending-order-with-null-at-the-end)
    * [Split string with a separator and get specific part](#split-string-with-a-separator-and-get-specific-part)
    * [Test with a list of values](#test-with-a-list-of-values)
    * [Where not like multiple values](#where-not-like-multiple-values)
    * [Get JSON object field as text](#get-json-object-field-as-text)
    * [Update a column from another table](#update-a-column-from-another-table)
    * [Convert new lines](#convert-new-lines)
    * [Select only first join match](#select-only-first-join-match)
    * [Round to closest 5 cents](#round-to-closest-5-cents)
    * [Get hourly data of the last month](#get-hourly-data-of-the-last-month)
    * [Remove null values in an array](#remove-null-values-in-an-array)
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
    * [Create MultiPolygon from outer ring of multiple polygons](#create-multipolygon-from-outer-ring-of-multiple-polygons)
    * [Move a point with a distance and an azimuth](#move-a-point-with-a-distance-and-an-azimuth)
    * [Find nearest point from another table](#find-nearest-point-from-another-table)
    * [Create point on the center of a linestring](#create-point-on-the-center-of-a-linestring)
    * [Get BBOX of all table content](#get-bbox-of-all-table-content)
* [Cryptography](#cryptography)
    * [Activate pgcrypto extension](#activate-pgcrypto-extension)
    * [Function sha1](#function-sha1)
* [Triggers](#triggers)
    * [Get parcel number](#get-parcel-number)
    * [Get parcels numbers](#get-parcels-numbers)
    * [Get absolute path](#get-absolute-path)
    * [Update a view](#update-a-view)
* [Sequences](#sequences)
    * [Set current value](#set-current-value)
    * [Get next value](#get-next-value)
* [Constraints](#constraints)
    * [Drop foreign key only if exists](#drop-foreign-key-only-if-exists)
    * [Set foreign key as deferred](#set-foreign-key-as-deferred)
* [Information schema](#information-schema)
    * [Get all tables](#get-all-tables)
    * [Get all views](#get-all-views)
    * [Get all columns](#get-all-columns)
    * [Get all triggers](#get-all-triggers)
    * [Get all sequences](#get-all-sequences)
    * [Get tables with wrong SRID](#get-tables-with-wrong-srid)
    * [Get tables with wrong geometry type](#get-tables-with-wrong-geometry-type)
    * [Get trigger definition](#get-trigger-definition)
* [Miscellaneous](#miscellaneous)
    * [Get PostGIS version](#get-postgis-version)
    * [Set schema](#set-schema)
    * [Disconnect users](#disconnect-users)
* [psql](#psql)
    * [Create database with template](#create-database-with-template)
    * [Create schema and allow rights](#create-schema-and-allow-rights)
    * [Dump and restore database](#dump-and-restore-database)
* [Backup and restore](#backup-and-restore)
    * [Backup in custom format](#backup-in-custom-format)
    * [Backup specific schemas](#backup-specific-schemas)
    * [Restore backup](#restore-backup)
    * [Extract plain SQL schema from compressed backup](#extract-plain-sql-schema-from-compressed-backup)
* [Log](#log)
    * [pgBadger](#pgbadger)
* [PL/pgSQL](#plpgsql)
    * [Display non empty tables with number of rows](#display-non-empty-tables-with-number-of-rows)

## Tables

### Create table

```sql
CREATE TABLE <schema>.<table> (id serial PRIMARY KEY);
COMMENT ON TABLE <schema>.<table> IS '<comment>';
```

## Create table from a query

```sql
CREATE TABLE <schema>.<table> AS
SELECT * FROM <schema>.<table-or-view>;
```

### Create index

```sql
CREATE INDEX <table>_<column>_idx
ON <schema>.<table>
USING btree (<column>);
```

### Change table schema

```sql
ALTER TABLE <schema>.<table> SET SCHEMA <new-schema>;
```

## Data types

| Type          | Name                                       |
| ------------- | ------------------------------------------ |
| **Character** | `varchar(255)`, `varchar(50)`, `text`      |
| **Numeric**   | `int4`, `float8`                           |
| **Boolean**   | `bool`                                     |
| **Date/Time** | `date`, `timestamp`                        |
| **Geometry**  | `Point`, `MultiLineString`, `MultiPolygon` |

### Create UUID field

```
ALTER TABLE <schema>.<table> ADD COLUMN uuid uuid UNIQUE DEFAULT gen_random_uuid();
```

*QGIS* default value: `uuid('WithoutBraces')`

### Convert integer to UUID

```
ALTER TABLE <schema>.<table> ALTER COLUMN <column> TYPE text;
ALTER TABLE <schema>.<table> ALTER COLUMN <column> TYPE uuid USING <column>::uuid;
```

## Geometries

### Activate PostGIS extension

```sql
CREATE EXTENSION postgis;
```

### Create column

```sql
ALTER TABLE <schema>.<table> ADD COLUMN geom geometry(<Point|MultiLineString|MultiPolygon>, 2056);
```

### Insert geometry from text

```sql
INSERT INTO <schema>.<table> (geom) VALUES (ST_GeomFromText('POINT (<coord_y> <coord_x>)', 2056))
```

### Create spatial index

```sql
CREATE INDEX <table>_geom_idx
ON <schema>.<table>
USING gist (geom);
```

### Convert simple geometry to multi geometry

```sql
SELECT ST_Multi(geom)::Geometry(<MultiLineString|MultiPolygon>, 2056) AS geom
FROM <table>;
```

See [convert_simple_geometry_to_multi.sql](../code/sql/convert_simple_geometry_to_multi.sql)

### Convert MultiPoint to Point

```sql
SELECT (ST_Dump(geom)).geom::Geometry(Point, 2056) AS geom
FROM <table>;
```

### Change projection

```sql
SELECT ST_Transform(geom, 2056)::Geometry(<Point|MultiLineString|MultiPolygon>, 2056) AS geom
FROM <table>;
```

### Set table geometry and projection

```sql
ALTER TABLE <table> ALTER COLUMN geom TYPE geometry(<Point|MultiLineString|MultiPolygon>, 2056);
```

### Create polygon with closed linestrings

```sql
SELECT ST_MakePolygon((ST_Dump(geom)).geom) AS geom
FROM <table>
WHERE ST_IsClosed(geom);
```

### Create point on the center of a linestring

```
SELECT ST_ClosestPoint(geom, ST_Centroid(geom))
FROM <table>;
```

## Queries

### Create an unique id

```sql
SELECT ROW_NUMBER() OVER (ORDER BY <column>) AS id
FROM <table>;
```

### Set first character to uppercase

```sql
SELECT ((UPPER(SUBSTR(<column>, 1, 1)) || SUBSTR(<column>, 2)))::varchar AS <column>
FROM <table>;
```

### Change text to uppercase

Removing accents

```sql
SELECT UPPER(UNACCENT(<column>))::varchar AS <column>
FROM <table>;
```

Keeping accents

```sql
SELECT UPPER(<column> COLLATE "fr-CH-x-icu")::varchar AS <column>
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

### Concatenate strings in an aggregate expression

```sql
SELECT company_id, STRING_AGG(employee, ', ' ORDER BY employee)
FROM <table>
GROUP BY company_id;
```

### Split values into rows

```sql
SELECT id, REGEXP_SPLIT_TO_TABLE(no_parcelle, ';') AS no_parcelle
FROM <table>;
```

### Add an unit to a value

```sql
SELECT (ROUND(length::numeric, 2) || ' m')::varchar AS length
FROM <table>;
```

### Convert numeric to string

```sql
SELECT
    TRIM(TO_CHAR(p.numero::numeric, '9999 999 9'))::varchar(20) AS numero,
    TRIM(TO_CHAR(ST_X(p.geom), '999G999.99 m'))::varchar(20) AS coord_y,
    TRIM(TO_CHAR(ST_Y(p.geom), '999G999.99 m'))::varchar(20) AS coord_x,
    TRIM(TO_CHAR(p.geomalt, '9G999.99 m'))::varchar(20) AS altitude
FROM mo.mo_pfp1 p;
```

### Convert date to string

```sql
SELECT to_char(<column>, 'DD.MM.YYYY') AS <column>
FROM <table>;
```

### Convert string to date

```sql
SELECT to_date(<column>, 'DD.MM.YYYY') AS <column>
FROM <table>;
```

### Get previous business day

```sql
SELECT
    CASE (EXTRACT(ISODOW FROM current_date)::integer) % 7
        WHEN 1 THEN current_date - 3
        WHEN 0 THEN current_date - 2
        ELSE current_date - 1
    END AS previous_business_day;
```

### Get next business day

```sql
SELECT
    CASE (EXTRACT(ISODOW FROM current_date)::integer) % 7
        WHEN 5 THEN current_date + 3
        WHEN 6 THEN current_date + 2
        ELSE current_date + 1
    END AS next_business_day;
```

### Sort results by list

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

### Sort results by varchar as numeric

```sql
SELECT *
FROM <table>
ORDER BY nullif(regexp_replace(<column>, '\D', '', 'g'), '')::int;
```

### Sort results by descending order with null at the end

```sql
SELECT *
FROM <table>
ORDER BY <column> DESC NULLS LAST;
```

### Split string with a separator and get specific part

```sql
SELECT (REGEXP_SPLIT_TO_ARRAY(<attribute>, '/'))[3] AS <column>
FROM <table>;
```

### Test with a list of values

```sql
SELECT *
FROM <table>
WHERE <attribute> SIMILAR TO '(<value1>|<value2>|<value3>)';
```

### Where not like multiple values

```sql
SELECT *
FROM <table>
WHERE <attribute> NOT LIKE ALL (ARRAY['%<pattern1>%', '%<pattern2>%']);
```

### Get JSON object field as text

```sql
SELECT '{"format":"GPKG", "projection":"SWITZERLAND95"}'::json->>'projection' AS projection;
```

### Update a column from another table

```sql
UPDATE <table1>
SET <column> = <table2>.<column>
FROM <table2>
WHERE <table1>.<fk> = <table2>.id;
```

### Convert new lines

```sql
SELECT regexp_replace(<column>, '[\n\r]+', '<br />', 'g') AS <column>,
```

### Select only first join match

```sql
SELECT DISTINCT ON (<unique-column>)
    t1.*,
    t2.*
FROM <table1> t1
LEFT JOIN <table2> t2 ON t2.fk = t1.pk
ORDER BY <unique-column> -- IMPORTANT
```

### Round to closest 5 cents

```sql
SELECT round(<amount> / 5, 2) * 5 AS <column>
FROM <table>;
```

### Get hourly data of the last month

```sql
SELECT *
FROM <table>
WHERE <datetime> >= date_trunc('hour', CURRENT_DATE - INTERVAL '1 month')
AND <datetime> <= date_trunc('hour', CURRENT_DATE)
AND EXTRACT(MINUTE FROM <datetime>) = 0
AND EXTRACT(SECOND FROM <datetime>) = 0
ORDER BY <datetime>;
```

### Remove null values in an array

```sql
SELECT ARRAY_REMOVE(<array>, NULL) AS <array>
FROM <table>;
```

## Spatial queries

### Spatial join (point in polygon)

```sql
SELECT *
FROM <table1> a, <table2> b
WHERE ST_Within(a.geom, b.geom);
```

### Create a line between two points

```sql
SELECT ST_MakeLine(a.geom, b.geom)::Geometry(LineString, 2056) AS geom
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
SELECT <attribute>, ST_Union(ST_SnapToGrid(geom, 0.0001))::Geometry(MultiPolygon, 2056) AS geom
FROM <table>
GROUP BY <attribute>;
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
SELECT ST_OffsetCurve((ST_Dump(geom)).geom::Geometry(LineString, 2056), <offset>)::Geometry(MultiLineString, 2056) AS geom
FROM <table>;
```

### Create a zone with buffers

```sql
SELECT ST_Multi(ST_Union(ST_SnapToGrid(ST_Buffer(geom, <radius>), 0.0001)))::Geometry(MultiPolygon, 2056) AS geom
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
        ST_PointN((ST_Dump(geom)).geom, 1)::Geometry(Point, 2056) as p1,
        ST_PointN((ST_Dump(geom)).geom, 2)::Geometry(Point, 2056) as p2
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

### Create MultiPolygon from outer ring of multiple polygons

```sql
SELECT ST_Multi(ST_MakePolygon(ST_ExteriorRing(ST_Union(geom))))::geometry(MultiPolygon, 2056) AS geom
FROM <table>
```

### Move a point with a distance and an azimuth

```sql
SELECT ST_Transform(ST_Project(ST_Transform(geom, 4326), <distance>, <azimuth>)::Geometry, 2056)::Geometry(Point, 2056) AS geom
FROM <table>;
```

### Find nearest point from another table

With:

* `<->` as distance between bbox centers
* `<#>` as distance between bbox edges

```sql
SELECT a.id,
(
    SELECT b.id
    FROM <table2> b
    ORDER BY a.geom <#> b.geom
    LIMIT 1
)
FROM <table1> a;
```

### Get BBOX of all table content

```sql
SELECT
    MIN(ST_XMin(geom)) AS l,
    MIN(ST_YMin(geom)) AS b,
    MAX(ST_XMax(geom)) AS r,
    MAX(ST_YMax(geom)) AS t
FROM <table>;
```

## Cryptography

### Activate pgcrypto extension

```sql
CREATE EXTENSION pgcrypto;
```

### Function sha1

```sql
CREATE OR REPLACE FUNCTION public.sha1(bytea)
RETURNS text AS
    $BODY$
        SELECT encode(digest($1, 'sha1'), 'hex')
    $BODY$
LANGUAGE sql IMMUTABLE STRICT;
```

## Triggers

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
    SELECT INTO new.no_parcelle string_agg(numero, ';' ORDER BY numero)
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

### Update a view

```sql
CREATE OR REPLACE FUNCTION <schema>.update_<view>()
    RETURNS trigger AS
        $BODY$
        BEGIN
            UPDATE <schema>.<table>
            SET
            <column1> = NEW.<column1>,
            <column2> = NEW.<column2>,
            <column3> = NEW.<column3>,
            WHERE id = OLD.id;
            RETURN NEW;
        RETURN NEW;
        END;

CREATE TRIGGER tr_update_<view>
INSTEAD OF UPDATE
ON <schema>.<view>
FOR EACH ROW
EXECUTE PROCEDURE <schema>.update_<view>();
```

## Sequences

### Set current value

```sql
SELECT setval('<schema>.<table>_<column>_seq', (SELECT MAX(<column>) FROM <schema>.<table>));
```

### Get next value

```sql
SELECT currval('<schema>.<table>_<column>_seq') + 1 AS next_<column>_val;
```

## Constraints

### Drop foreign key only if exists

```sql
ALTER TABLE <schema>.<table> DROP CONSTRAINT IF EXISTS <table>_<column>_fkey;
```

### Set foreign key as deferred

```sql
ALTER TABLE <schema>.<child_table>
ADD CONSTRAINT <child_table>_fk_<parent_table> FOREIGN KEY (fk_<parent_table>)
REFERENCES <schema>.<parent_table>(id)
ON UPDATE CASCADE ON DELETE <RESTRICT|CASCADE>
DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX <child_table>_fk_<parent_table>_idx ON <schema>.<child_table> (fk_<parent_table>);
```

`ON DELETE` action:
* `RESTRICT` for usual relation
* `CASCADE` for pivot table

## Information schema

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

### Get all columns

#### Tables

```sql
SELECT
    table_schema,
    table_name,
    ordinal_position AS position,
    column_name,
    data_type,
    CASE
        WHEN character_maximum_length IS NOT NULL
        THEN character_maximum_length
        ELSE numeric_precision
    END AS max_length,
    is_nullable,
    column_default AS default_value
FROM information_schema.columns
WHERE table_schema NOT IN ('information_schema', 'pg_catalog', 'public', 'topology')
ORDER BY table_schema, table_name, ordinal_position;
```

#### Views

```sql
SELECT
    t.table_schema AS schema_name,
    t.table_name AS view_name,
    c.column_name,
    c.data_type,
    CASE
        WHEN c.character_maximum_length IS NOT NULL
        THEN c.character_maximum_length
        ELSE c.numeric_precision
    END AS max_length,
    is_nullable
FROM information_schema.tables t
LEFT JOIN information_schema.columns c ON t.table_schema = c.table_schema AND t.table_name = c.table_name
WHERE t.table_type = 'VIEW'
AND t.table_schema NOT IN ('information_schema', 'pg_catalog', 'public', 'topology')
ORDER BY t.table_schema, t.table_name;
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
WHERE g.srid <> 2056
ORDER BY g.f_table_schema, g.f_table_name;
```

### Get tables with wrong geometry type

```sql
SELECT g.f_table_catalog, g.f_table_schema, g.f_table_name, g.f_geometry_column, g.coord_dimension, g.srid, g.type
FROM geometry_columns g
WHERE g.type NOT IN ('POINT', 'MULTILINESTRING', 'MULTIPOLYGON')
ORDER BY g.f_table_schema, g.f_table_name;
```

### Get trigger definition

```sql
SELECT pg_get_triggerdef(oid)
FROM pg_trigger
WHERE tgname = '<trigger>';
```

## Miscellaneous

### Get PostGIS version

```sql
SELECT PostGIS_full_version();
```

### Set schema

```bash
SET search_path = <schema>;
```

### Disconnect users

```bash
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE (datname = '<database>')
AND pid <> pg_backend_pid();
```

## psql

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

## Backup and restore

### Backup in custom format

```bash
pg_dump --format=custom --blobs <database> > <database>.backup
```

### Backup specific schemas

```bash
pg_dump --format=custom --blobs <database> --schema='<pattern>' > <database>.backup
```

### Restore backup

```bash
pg_restore --dbname=<database> <database>.backup
```

### Extract plain SQL schema from compressed backup

```bash
pg_restore --file <database>.sql --schema-only <database>.backup
```

## Log

### pgBadger

```bash
cd /d <path-to-postgres-data>\pg_log
dir postgresql-<YYYY-MM>-* /b > list-<YYYY-MM>.txt
perl "<path-to-pgbadger>\pgbadger" --exclude-time "^* (20|21|22|23):*" --exclude-query="^(COPY|COMMIT|FETCH|VACUUM)" --disable-checkpoint --disable-lock --disable-temporary --disable-autovacuum --outfile postgresql-<YYYY-MM>.html --logfile-list list-<YYYY-MM>.txt
del list-<YYYY-MM>.txt
```

## PL/pgSQL

### Display non empty tables with number of rows

```sql
DO $$
DECLARE
    tbl RECORD;
    row_count BIGINT;
    schema_name TEXT := '<schema>';
BEGIN
    FOR tbl IN
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = schema_name
        AND table_type = 'BASE TABLE'
        ORDER BY table_name
    LOOP
        EXECUTE format('SELECT COUNT(*) FROM %I.%I', schema_name, tbl.table_name) INTO row_count;
        IF row_count > 0 THEN
            RAISE NOTICE 'Table %: % rows', tbl.table_name, row_count;
        END IF;
    END LOOP;
END $$;
```

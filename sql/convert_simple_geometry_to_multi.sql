-- Polygon to MultiPolygon
ALTER TABLE <schema>.<table> RENAME geom TO geom_old;
ALTER TABLE <schema>.<table> ADD COLUMN geom geometry(MultiPolygon, 21781);
UPDATE <schema>.<table> SET geom = ST_Multi(geom_old) :: Geometry(MultiPolygon, 21781);
CREATE INDEX <table>_geom_idx ON <schema>.<table> USING gist (geom);
ALTER TABLE <schema>.<table> DROP COLUMN geom_old;

-- LineString to MultiLineString
ALTER TABLE <schema>.<table> RENAME geom TO geom_old;
ALTER TABLE <schema>.<table> ADD COLUMN geom geometry(MultiLineString, 21781);
UPDATE <schema>.<table> SET geom = ST_Multi(geom_old) :: Geometry(MultiLineString, 21781);
CREATE INDEX <table>_geom_idx ON <schema>.<table> USING gist (geom);
ALTER TABLE <schema>.<table> DROP COLUMN geom_old;

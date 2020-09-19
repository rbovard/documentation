# osm2pgsql

* [Import data](#import-data)

## Import data

```batchfile
set pgpassword=<password>
osm2pgsql -s -H <host> -P <port> -U <user> -d <database> -S default.style -p <file> <file>.osm.pbf
```

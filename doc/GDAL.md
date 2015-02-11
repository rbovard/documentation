GDAL
====

gdaltindex
----------

Use files in subfolders

```batchfile
dir /s/b *.tif > list.txt
gdaltindex tiles.shp --optfile list.txt
```

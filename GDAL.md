GDAL
====

gdaltindex
----------

```
-- Use files in subfolders for `gdaltindex`
dir /s/b *.tif > list.txt
gdaltindex tiles.shp --optfile list.txt
```

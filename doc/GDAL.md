GDAL
====

* [gdaltindex](#gdaltindex)
* [gdal_rasterize](#gdal_rasterize)
* [gdal_translate](#gdal_translate)

gdaltindex
----------

Use files in subfolders

```batchfile
dir /s/b *.tif > list.txt
gdaltindex tiles.shp --optfile list.txt
del list.txt
```

gdal_rasterize
--------------

```batchfile
gdal_rasterize -l <file> -a <attribute> -tr <resolution>.0 <resolution>.0 -a_nodata 0 -ot Int32 <file>.shp <file>.tif
```

gdal_translate
--------------

GeoTIFF > Binary Terrain

```batchfile
gdal_translate -of bt <file>.tif <file>.bt
```

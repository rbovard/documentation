GDAL
====

* [Build raster tileindex](#build-raster-tileindex)
* [Generate raster grid](#generate-raster-grid)
* [Convert data](#convert-data)
    * [GeoTIFF to Binary Terrain](#geotiff-to-binary-terrain)

Build raster tileindex
----------------------

```batchfile
dir /s/b *.tif > list.txt
gdaltindex tiles.shp --optfile list.txt
del list.txt
```

Generate raster grid
--------------------

```batchfile
gdal_rasterize -l <file> -a <attribute> -tr <resolution>.0 <resolution>.0 -a_nodata 0 -ot Int32 <file>.shp <file>.tif
```

Convert data
------------

### GeoTIFF to Binary Terrain

```batchfile
gdal_translate -of bt <file>.tif <file>.bt
```

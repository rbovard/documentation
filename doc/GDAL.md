GDAL
====

Raster
------

* [Optimize GeoTIFF files](#optimize-geotiff-files)
* [Build raster tileindex](#build-raster-tileindex)
* [Rasterize vector data](#rasterize-vector-data)
* [Polygonize raster grid](#polygonize-raster-grid)
* [Convert raster data](#convert-raster-data)
    * [GeoTIFF to Binary Terrain](#geotiff-to-binary-terrain)

Vector
------

* [Convert vector data](#convert-vector-data)
    * [Usage](#usage)
    * [Formats](#formats)
    * [Options](#options)

Optimize GeoTIFF files
----------------------

Create tiled file and build overview images

```batchfile
gdal_translate -of GTiff -co "TILED=YES" -co "TFW=YES" <source>.tif <file>.tif
gdaladdo -r average <file>.tif 2 4 8 16
```

See [optimize_raster.py](../python/optimize_raster.py)

Build raster tileindex
----------------------

```batchfile
dir /s/b *.tif > list.txt
gdaltindex tiles.shp --optfile list.txt
del list.txt
```

Rasterize vector data
---------------------

```batchfile
gdal_rasterize -l <file> -a <attribute> -tr <resolution>.0 <resolution>.0 -a_nodata 0 -ot Int32 <file>.shp <file>.tif
```

Polygonize raster grid
----------------------

```batchfile
gdal_polygonize <file>.tif -f "ESRI Shapefile" <file> <file>
```

Convert raster data
-------------------

### GeoTIFF to Binary Terrain

```batchfile
gdal_translate -of bt <file>.tif <file>.bt
```

See [convert_to_bt.py](../python/convert_to_bt.py)

Convert vector data
-------------------

### Usage

```batchfile
ogr2ogr -f "<format>" [options] <dst_datasource_name> <src_datasource_name>
```

### Formats

* ESRI Shapefile: `ESRI Shapefile`
* GeoJSON: `GeoJSON`

### Options

* -t_srs: Reproject to SRS (`-t_srs EPSG:<code>`)
* -select: List of fields (`-select "<field1>, <field2>"`)
* -where: Attribute query (`-where "<field> = '<value>'"`)

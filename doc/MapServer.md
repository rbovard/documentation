MapServer
=========

* [Optimization](#optimization)
    * [Layer](#layer)
    * [Projection](#projection)
    * [Class](#class)
    * [Expressions](#expressions)
    * [Raster](#raster)
* [Miscellaneous](#miscellaneous)
    * [Get MapServer version](#get-mapserver-version)

Optimization
------------

### Layer

Define those parameters for each layer:

* `EXTENT`: To avoid to compute it on the fly
* `MAXSCALEDENOM`: To avoid to render data at all scales

### Projection

Remove all unneeded projection definitions from the EPSG database (`CONFIG "PROJ_LIB" "/path/to/epsg"`) to avoid to lookup all defintions at each query.

### Class

Place the most commonly-used classes at the top of the class list because classes are processed in order and a feature is assigned to the first class that matches.

### Expressions

#### Simple comparison

Use string comparison instead of regular expression comparison:

```
CLASSITEM "foo"
CLASS
    EXPRESSION "bar"
```

Instead of:

```
EXPRESSION ("[foo]" = "bar")
```

#### List expressions

Use list expressions to compare a string attribute to a list of multiple possible values instead of regex or mapserver expressions:

```
EXPRESSION {motorway,trunk}
```

Instead of:

```
# Regex expression
EXPRESSION /motorway|trunk/

# MapServer expression
EXPRESSION ("[roadtype]" IN "motorway,trunk")
```

### Raster

* Use tile indexes instead of multiple layers (`gdaltindex` to generate it), with `TILEINDEX` and `TILEITEM`
* Use tiled TIFF files (`gdal_translate -of GTiff -co "TILED=YES"`) and build overview images (`gdaladdo -r average`)

See [optimize_raster.py](../python/optimize_raster.py)

Miscellaneous
-------------

### Get mapserver version

```bash
/usr/lib/cgi-bin/mapserv -v
```

FME
===

* [Transformers](#Transformers)
    * [Remove geometry dimension](#remove-geometry-dimension)
    * [Convert GeometryCollection to MultiPolygon or MultiLineString](#convert-geometrycollection-to-multipolygon-or-multilinestring)
    * [Create an unique identifier](#create-an-unique-identifier)
* [Batch process](#batch-process)
    * [Use multiple source datasets](#use-multiple-source-datasets)
* [String replacer](#string-replacer)
    * [Add thousand separator](#add-thousand-separator)
* [Python scripts](#python-scripts)
    * [Check if file exists](#check-if-file-exists)
    * [Remove accents](#remove-accents)
* [Expressions](#expressions)
    * [Check if attribute is integer](#check-if-attribute-is-integer)
* [Coordinates systems](#coordinates-systems)
    * [Projections](#projections)
    * [Transformers](#transformers)

Transformers
------------

### Remove geometry dimension

* Elevation: `2DForcer`
* Measure: `MeasureRemover`

### Convert GeometryCollection to MultiPolygon or MultiLineString

* `GeometryRefiner`

### Create an unique identifier

* `CRCCalculator`

Batch process
-------------

### Use multiple source datasets

```batchfile
for %%f in (*.ext) do fme <workspace>.fmw --parameter "%%f"
```

String replacer
---------------

### Add thousand separator

* Mode: *Replace regular expression*
* Text to replace: `(?<=\d)(?=(\d\d\d)+(?!\d))`
* Replacemeent text: `'`

Python scripts
--------------

### Check if file exists

```python
import fmeobjects
import os

def processFeature(feature):
    doesFileExist = os.path.exists(feature.getAttribute("path"))
    feature.setAttribute("file_exists", doesFileExist)
```

### Remove accents

```python
import fmeobjects
import unicodedata as ud

def rmdiacritics(char):
    '''
    Return the base character of char, by "removing" any
    diacritics like accents or curls and strokes and the like.
    '''
    desc = ud.name(unicode(char))
    cutoff = desc.find(' WITH ')
    if cutoff != -1:
        desc = desc[:cutoff]
    return ud.lookup(desc)

def removeAccents(feature):
    attribute_list = ("name", "type", "state") # Modify as needed
    for attrib in feature.getAllAttributeNames():
        if attrib in attribute_list:
            value = feature.getAttribute(attrib)
            if value:
                value = unicode(value)
                new_value = ''.join([rmdiacritics(char) for char in value])
                feature.setAttribute(attrib, new_value)
```

Expressions
-----------

### Check if attribute is integer

```python
(@Value(attribute) == int(@Value(attribute))) ? 1 : 0
```

Coordinates systems
-------------------

### Projections

MN03
- `EPSG:21781`
- CH1903 / LV03

MN95
- `EPSG:2056`
- CH1903+ / LV95 (Swiss CH1903+ / LV95)

### Transformers

ReframeReprojector
- FINELTRA (`reframereproject.dll`)
- Triangles
- ~ cm

Reprojector
- NTv2 (`CHENYX06.gsb`)
- Grids
- ~ dm

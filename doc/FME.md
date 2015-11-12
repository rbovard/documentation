FME
===

* [Batch process](#batch-process)
    * [Use multiple source datasets](#use-multiple-source-datasets)
* [Python scripts](#python-scripts)
    * [Check if file exists](#check-if-file-exists)
* [Expressions](#expressions)
    * [Check if attribute is integer](#check-if-attribute-is-integer)
* [Remove geometry dimension](#remove-geometry-dimension)
* [Coordinates systems](#coordinates-systems)
    * [Projections](#projections)
    * [Transformers](#transformers)

Batch process
-------------

### Use multiple source datasets

```batchfile
for %%f in (*.ext) do fme <workspace>.fmw --parameter "%%f"
```

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

Expressions
-----------

### Check if attribute is integer

```python
(@Value(attribute) == int(@Value(attribute))) ? 1 : 0
```

Remove geometry dimension
-------------------------

* Elevation: `2DForcer`
* Measure: `MeasureRemover`

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

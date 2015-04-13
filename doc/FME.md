FME
===

* [Batch process](#batch-process)
    * [Use multiple source datasets](#use-multiple-source-datasets)
* [Python scripts](#python-scripts)
    * [Check if file exists](#check-if-file-exists)
* [Expressions](#expressions)
    * [Check if attribute is integer](#check-if-attribute-is-integer)
* [Remove geometry dimension](#remove-geometry-dimension)

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

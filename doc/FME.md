FME
===

* [Batch process](#batch-process)
* [Python scripts](#python-scripts)
* [Expressions](#expressions)

Batch process
-------------

Use multiple source datasets

```batchfile
for %%f in (*.ext) do fme workspace.fmw --parameter "%%f"
```

Python scripts
--------------

Check if file exists

```python
import fmeobjects
import os

def processFeature(feature):
    doesFileExist = os.path.exists(feature.getAttribute("path"))
    feature.setAttribute("file_exists", doesFileExist)
```

Expressions
-----------

Check if attribute is integer

```python
(@Value(attribute) == int(@Value(attribute))) ? 1 : 0
```

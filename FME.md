FME
===

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

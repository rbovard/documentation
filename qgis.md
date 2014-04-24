QGIS
====

Settings
--------

```python
from PyQt4.QtCore import QSettings
s = QSettings()

# Display all settings
for k in s.allKeys(): print k, ":", s.value(k)

# Read a setting
s.value("Qgis/stylesheet/fontFamily")

# Write a setting
s.setValue("Qgis/stylesheet/fontFamily", u"Arial")
```

### Default settings

To run QGIS with default settings, add the command line option ```--optionspath``` at the end of the target in ```%ProgramFiles%\QGIS <version>\bin\qgis.bat```:

```batchfile
qgis-bin.exe --optionspath c:/temp/qgis
```

A new settings file will be created (```QGIS/QGIS2.ini```) and used instead of the stored ```QSettings```.

> With the command line option ```--configpath```, QGIS will use the given path for all user configuration (```QSettings``` and ```.qgis2``` folder).

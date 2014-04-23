QGIS
====

PyQGIS
------

### Settings

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

QGIS
====

Actions
-------

| Name         | Type | Action |
| ------------ | ---- | ------ |
| PDF          | Open | ```"[% "file" %]"``` |
| RF simplifié | Open | ```http://www.rfinfo.vd.ch/rfinfo.php?no_commune=[%substr("IDENTDN", 4, 3)%]&no_immeuble=[%"numero"%]``` |
| RF complet   | Open | ```https://secure.vd.ch/territoire/intercapi/faces?bfs=[%substr("IDENTDN", 4, 3)%]&kr=0&n1=[%"numero"%]&type=grundstueck_grundbuch_auszug&sec=<key>&intercapi=Extrait+RF+online``` |

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

To run QGIS with default settings, add the command line option `--optionspath` at the end of the target in `%ProgramFiles%\QGIS <version>\bin\qgis.bat`:

```batchfile
qgis-bin.exe --optionspath c:/temp/qgis
```

> For Linux, simply use:
>
>```bash
>qgis --optionspath /tmp/qgis
>```

A new settings file will be created (`QGIS/QGIS2.ini`) and used instead of the stored `QSettings`.

> With the command line option `--configpath`, QGIS will use the given path for all user configuration (`QSettings` and `.qgis2` folder).

Message bar
-----------

```python
from qgis.gui import *

message = u"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

iface.messageBar().pushMessage("Information", message, level=QgsMessageBar.INFO, duration=3)
iface.messageBar().pushMessage("Warning", message, level=QgsMessageBar.WARNING)
iface.messageBar().pushMessage("Error", message, level=QgsMessageBar.CRITICAL)
```

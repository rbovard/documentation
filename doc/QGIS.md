QGIS
====

* [Actions](#actions)
* [Atlas](#atlas)
    * [Display only current altlas attribute related features](#display-only-current-altlas-attribute-related-features)
    * [Display number of features in current atlas](#display-number-of-features-in-current-atlas)
* [Settings](#settings)
    * [Default settings](#default-settings)
* [Message bar](#message-bar)
* [Toolbar](#toolbar)
* [Installation](#installation)

Actions
-------

| Name         | Type | Action |
| ------------ | ---- | ------ |
| PDF          | Open | ```"[% "file" %]"``` |
| RF simplifié | Open | ```http://www.rfinfo.vd.ch/rfinfo.php?no_commune=[%substr("IDENTDN", 4, 3)%]&no_immeuble=[%"numero"%]``` |
| RF complet   | Open | ```https://secure.vd.ch/territoire/intercapi/faces?bfs=[%substr("IDENTDN", 4, 3)%]&kr=0&n1=[%"numero"%]&type=grundstueck_grundbuch_auszug&sec=<key>&intercapi=Extrait+RF+online``` |

Atlas
-----

### Display only current altlas attribute related features

With a rule based symbology

```
<attribute> = attribute(@atlas_feature , '<attribute>')
```

### Display number of features in current atlas

```
aggregate('<layer>', 'count', 'id', intersects(@atlas_geometry, $geometry))
```

Settings
--------

```python
from PyQt4.QtCore import QSettings

settings = QSettings()

# Display all settings
for k in settings.allKeys(): print k, ":", settings.value(k)

# Read a setting
settings.value("<setting>")

# Write a setting
settings.setValue("<setting>", u"<value>")
```

### Default settings

To run QGIS with default settings, add the command line option `--optionspath` at the end of the target in `%ProgramFiles%\QGIS <version>\bin\qgis.bat`:

```batchfile
qgis-bin.exe --optionspath C:\Temp
```

> For Linux, simply use:
>
>```bash
>qgis --optionspath /tmp
>```

A new settings file will be created (`QGIS/QGIS2.ini`) and used instead of the stored `QSettings`.

> With the command line option `--configpath`, QGIS will use the given path for all user configuration (`QSettings` and `.qgis2` folder).

Message bar
-----------

```python
from qgis.gui import *

message = u"<message>"

iface.messageBar().pushMessage("Information", message, level=QgsMessageBar.INFO, duration=3)
iface.messageBar().pushMessage("Warning", message, level=QgsMessageBar.WARNING)
iface.messageBar().pushMessage("Error", message, level=QgsMessageBar.CRITICAL)
```

Toolbar
-------

```python
from PyQt5.QtWidgets import QToolBar
for x in iface.mainWindow().findChildren(QToolBar): print(x.objectName())
```

Installation
------------

### Alternative repository

File `/etc/apt/sources.list`

```bash
## QGIS stable
deb http://qgis.org/debian xenial main
deb-src http://qgis.org/debian xenial main

## QGIS nightly
#deb http://qgis.org/debian-nightly xenial main
#deb-src http://qgis.org/debian-nightly xenial main
```

Key

```bash
wget -O - http://qgis.org/downloads/qgis-2016.gpg.key | gpg --import
gpg --fingerprint 073D307A618E5811
gpg --export --armor 073D307A618E5811 | sudo apt-key add -
```

### Installation

QGIS

```bash
sudo apt update
sudo apt install qgis python-qgis
```

Dev tools

```bash
sudo apt install pyqt4-dev-tools qt4-designer
```

QGIS
====

* [Actions](#actions)
* [Settings](#settings)
    * [Default settings](#default-settings)
* [Message bar](#message-bar)
* [Installation](#installation)

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

message = u"<message>"

iface.messageBar().pushMessage("Information", message, level=QgsMessageBar.INFO, duration=3)
iface.messageBar().pushMessage("Warning", message, level=QgsMessageBar.WARNING)
iface.messageBar().pushMessage("Error", message, level=QgsMessageBar.CRITICAL)
```

Installation
------------

### Alternative repository

File `/etc/apt/sources.list`

```bash
## QGIS stable
deb http://qgis.org/debian trusty main
deb-src http://qgis.org/debian trusty main

## QGIS nightly
#deb http://qgis.org/debian-nightly trusty main
#deb-src http://qgis.org/debian-nightly trusty main
```

### Installation

Key

```bash
gpg --keyserver keyserver.ubuntu.com --recv DD45F6C3
gpg --export --armor DD45F6C3 | sudo apt-key add -
```

QGIS

```bash
sudo apt update
sudo apt install qgis python-qgis
```

Dev tools

```bash
sudo apt install pyqt4-dev-tools qt4-designer
```

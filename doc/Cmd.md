Cmd
===

* [Directories and files](#directories-and-files)
    * [Delete directory](#delete-directory)
    * [Copy directory](#copy-directory)
* [Applications](#applications)
    * [Start installation](#start-installation)
* [Fonts](#fonts)
    * [Install font](#install-font)
* [Batch scripts](#batch-scripts)
    * [Echo](#echo)
    * [Remark](#remark)

Directories and files
---------------------

### Delete directory

```batchfile
IF EXIST %USERPROFILE%\.qgis2\python\plugins\SettingsManager RD %USERPROFILE%\.qgis2\python\plugins\SettingsManager /S /Q
```

### Copy directory

```batchfile
XCOPY \\orcus\SITNyon\Geodata\Outils\Plugins\.qgis2 %USERPROFILE%\.qgis2 /E /I /Q /Y
```

Applications
------------

### Start installation

```batchfile
START /WAIT QGIS-OSGeo4W-2.8.1-1-Setup-x86.exe
```

Fonts
-----

### Install font

```batchfile
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /v "Cadastra.ttf (TrueType)" /t REG_SZ /d "Cadastra.ttf" /f
```

Batch scripts
-------------

### Echo

```batchfile
@ECHO OFF
```

### Remark

```batchfile
REM Text
```

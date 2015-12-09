Cmd
===

* [Directories and files](#directories-and-files)
    * [Delete directory](#delete-directory)
    * [Copy directory](#copy-directory)
* [Applications](#applications)
    * [Start installation](#start-installation)
    * [Run batch](#run-batch)
* [Fonts](#fonts)
    * [Install font](#install-font)
* [Batch scripts](#batch-scripts)
    * [Echo](#echo)
    * [Remark](#remark)
    * [Wait](#wait)

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

### Run batch

```batchfile
call <batch>.bat
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

### Wait

```batchfile
ping 1.1.1.1 -n 1 -w 5000 >NUL
```

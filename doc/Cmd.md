Cmd
===

* [Directories and files](#directories-and-files)
    * [Delete directory](#delete-directory)
    * [Copy directory](#copy-directory)
    * [Backup directory](#backup-directory)
    * [List all specific files](#list-all-specific-files)
    * [List all files](#list-all-files)
    * [Delete files from a list](#delete-files-from-a-list)
* [Applications](#applications)
    * [Start installation](#start-installation)
    * [Run batch](#run-batch)
* [Fonts](#fonts)
    * [Install font](#install-font)
* [Batch scripts](#batch-scripts)
    * [Echo](#echo)
    * [Remark](#remark)
    * [Wait](#wait)
    * [Time](#time)
    * [Prompt variable](#prompt-variable)
* [Terminal server](#terminal-server)
    * [Disconnect user](#disconnect-user)
    * [Restart server](#restart-server)

Directories and files
---------------------

### Delete directory

```batchfile
IF EXIST %USERPROFILE%\.qgis2\python\plugins\SettingsManager RD %USERPROFILE%\.qgis2\python\plugins\SettingsManager /S /Q
```

### Delete all directories

```batchfile
dir *. /b > <list>.txt
for /f %%a in (<list>.txt) do (
    RD %%a /S /Q
)
del <list>.txt
```

### Copy directory

```batchfile
XCOPY \\orcus\SITNyon\Geodata\Outils\Plugins\.qgis2 %USERPROFILE%\.qgis2 /E /I /Q /Y
```

### Backup directory

```batchfile
XCOPY <source> <destination> /E /Y /D
```

### List all specific files

```batchfile
dir /s /b *.<ext> > <list>.txt
```

With date of last modification

```batchfile
for /f "delims=" %a in ('dir /s /b *.<ext>') do @echo %~ta %~a
```

### List all files

```batchfile
dir /s /b /a-d * > <list>.txt
```

### Delete files from a list

```
for /f %i in (<list>.txt) do del %i
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

#### Empty line

```batchfile
ECHO:
```

### Remark

```batchfile
:: Text
```

### Wait

```batchfile
ping 1.1.1.1 -n 1 -w 5000 >NUL
```

### Time

```batchfile
ECHO %time%
```

### Prompt variable

```batchfile
SET my_var=
SET /P my_var="My var: "
```

Terminal server
---------------

### Disconnect user

```batchfile
query session /server:<server>
reset session <id> /server:<server>
```

### Restart server

```batchfile
shutdown /r
```

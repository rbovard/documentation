# Cmd

* [Directories and files](#directories-and-files)
    * [Change directory and drive](#change-directory-and-drive)
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
    * [Pause](#pause)
    * [Remark](#remark)
    * [Wait](#wait)
    * [Time](#time)
    * [Prompt variable](#prompt-variable)
* [Terminal server](#terminal-server)
    * [Disconnect user](#disconnect-user)
    * [Restart server](#restart-server)
* [Environment variables](#environment-variables)
    * [Set environment variable](#set-environment-variable)
    * [Environment variables](#environment-variables)

## Directories and files

### Change directory and drive

```batchfile
CD /d <drive>:\<path>
```

### Delete directory

```batchfile
IF EXIST %USERPROFILE%\.qgis2\python\plugins\SettingsManager RD %USERPROFILE%\.qgis2\python\plugins\SettingsManager /S /Q
```

### Delete all directories

```batchfile
DIR *. /b > <list>.txt
FOR /f %%a IN (<list>.txt) DO (
    RD %%a /S /Q
)
DEL <list>.txt
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
DIR /s /b *.<ext> > <list>.txt
```

With date of last modification

```batchfile
FOR /f "delims=" %a IN ('DIR /s /b *.<ext>') DO @echo %~ta %~a
```

### List all files

```batchfile
DIR /s /b /a-d * > <list>.txt
```

### Delete files from a list

```
FOR /f %i IN (<list>.txt) DO DEL %i
```

## Applications

### Start installation

```batchfile
START /WAIT QGIS-OSGeo4W-2.8.1-1-Setup-x86.exe
```

### Run batch

```batchfile
CALL <batch>.bat
```

## Fonts

### Install font

```batchfile
REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" /v "Cadastra.ttf (TrueType)" /t REG_SZ /d "Cadastra.ttf" /f
```

## Batch scripts

### Echo

```batchfile
@ECHO OFF
```

### Pause

```batchfile
PAUSE
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
PING 1.1.1.1 -n 1 -w 5000 >NUL
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

## Terminal server

### Disconnect user

```batchfile
QUERY session /server:<server>
RESET session <id> /server:<server>
```

### Restart server

```batchfile
SHUTDOWN /r
```

## Environment variables

### Set environment variable

User:

```batchfile
SETX <variable> "<value>"
```

System (with admin privileges):

```batchfile
SETX <variable> "<value>" /M
```

### Environment variables

* `%AllUsersProfile%`: `C:\ProgramData`
* `%AppData%`: `C:\Users\<username>\AppData\Roaming`
* `%CommonProgramFiles%`: `C:\Program Files\Common Files`
* `%CommonProgramFiles(x86)%`: `C:\Program Files (x86)\Common Files`
* `%HomeDrive%`: `C:\`
* `%LocalAppData%`: `C:\Users\<username>\AppData\Local`
* `%ProgramData%`: `C:\ProgramData`
* `%ProgramFiles%`: `C:\Program Files` or `C:\Program Files (x86)`
* `%ProgramFiles(x86)%`: `C:\Program Files (x86)`
* `%Public%`: `C:\Users\Public`
* `%SystemDrive%`: `C:`
* `%SystemRoot%`: `C:\Windows`
* `%Temp%`: `C:\Users\<username>\AppData\Local\Temp`
* `%UserProfile%`: `C:\Users\<username>`

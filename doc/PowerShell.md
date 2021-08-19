# PowerShell

* [Directories and files](#directories-and-files)
    * [List files in directory](#list-files-in-directory)
    * [Rename a file](#rename-file)
    * [Open current location in Explorer](#open-current-location-in-explorer)

## Directories and files

### List files in directory

```powershell
Get-ChildItem -Path "<path>" -Name
```

### Rename file

```powershell
Rename-Item -Path "<path>\<to>\<file>" -NewName "<new-filename>"
```

### Open current location in Explorer

```powershell
Start .
```

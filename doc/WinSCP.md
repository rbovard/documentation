WinSCP
======

* [Execute script](#execute-script)
* [Scripts](#scripts)
    * [Connection](#connection)
    * [Synchronize folders](#synchronize-folders)
    * [Download specific file](#download-specific-file)

Execute script
--------------

```batchfile
@ECHO OFF
winscp.com /script=<script>.txt
```

Scripts
-------

### Connection

#### Open connection

```batchfile
option batch abort
option confirm off
open sftp://<user>@<server>:22/ -privatekey=<key>.ppk -hostkey="<fingerprint>"
```

#### Close connection

```batchfile
exit
```

### Synchronize folders

#### Specific files

```batchfile
synchronize local -filemask="<cne1>.*;<cne2>.*;<cne3>.*" <local_folder> <remote_folder>
```

#### Without file types

```batchfile
synchronize remote -filemask="|Thumbs.db" <local_folder> <remote_folder>
```

### Download specific file

```batchfile
get <file> <local_folder>\*
```

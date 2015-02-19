WinSCP
======

* [Download specific files](#download-specific-files)
* [Upload files](#upload-files)

Download specific files
-----------------------

### download.bat

```batchfile
@ECHO OFF
winscp.com /script=download.txt
```

### download.txt

```batchfile
option batch abort
option confirm off
open sftp://<user>@<server>:22/ -privatekey=<key>.ppk -hostkey="<fingerprint>"
synchronize local -filemask="<cne1>.*;<cne2>.*;<cne3>.*" <local_folder> <remote_folder>
exit
```

Upload files
------------

### upload.bat

```batchfile
@ECHO OFF
winscp.com /script=upload.txt
```

### upload.txt

```batchfile
option batch abort
option confirm off
open sftp://<user>@<server>:22/ -privatekey=<key>.ppk -hostkey="<fingerprint>"
synchronize remote -filemask="|Thumbs.db" <local_folder> <remote_folder>
exit
```

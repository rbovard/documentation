WinSCP
======

* [Execute script](#execute-script)
* [Download specific files](#download-specific-files)
* [Upload files](#upload-files)

Execute script
--------------

```batchfile
@ECHO OFF
winscp.com /script=<script>.txt
```

Download specific files
-----------------------

```batchfile
option batch abort
option confirm off
open sftp://<user>@<server>:22/ -privatekey=<key>.ppk -hostkey="<fingerprint>"
synchronize local -filemask="<cne1>.*;<cne2>.*;<cne3>.*" <local_folder> <remote_folder>
exit
```

Upload files
------------

```batchfile
option batch abort
option confirm off
open sftp://<user>@<server>:22/ -privatekey=<key>.ppk -hostkey="<fingerprint>"
synchronize remote -filemask="|Thumbs.db" <local_folder> <remote_folder>
exit
```

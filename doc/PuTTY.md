PuTTY
=====

* [SSH tunnel](#ssh-tunnel)
    * [Open SSH tunnel with port forwarding](#open-ssh-tunnel-with-port-forwarding)
    * [Close SSH tunnel](#close-ssh-tunnel)
* [Commands](#commands)
    * [Run commands](#run-commands)
    * [Run commands with output](#run-commands-with-output)
* [Settings](#settings)
    * [Export settings](#export-settings)

SSH tunnel
----------

### Open SSH tunnel with port forwarding

```batchfile
start "" "C:\Program Files\PuTTY\putty.exe" -ssh <user>@<server> -i <key>.ppk -L <local-port>:localhost:<remote-port>
ping 1.1.1.1 -n 1 -w 5000 >NUL
```

### Close SSH tunnel

```batchfile
taskkill /f /im putty.exe
```

Commands
--------

### Run commands

```batchfile
plink -ssh <user>@<server> -i <key>.ppk -m <commands>.sh
```

### Run commands with output

```batchfile
plink -ssh <user>@<server> -i <key>.ppk -m <commands>.sh > <output>.log
```

Settings
--------

### Export settings

```batchfile
regedit /e "%USERPROFILE%\Desktop\putty.reg" HKEY_CURRENT_USER\Software\SimonTatham
```

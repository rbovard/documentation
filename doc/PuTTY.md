PuTTY
=====

* [SSH tunnel](#ssh-tunnel)
    * [Open SSH tunnel with port forwarding](#open-ssh-tunnel-with-port-forwarding)
    * [Close SSH tunnel](#close-ssh-tunnel)
* [Run commands](#run-commands)

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

Run commands
------------

```batchfile
plink <putty-session> -l <user> -m <file>.sh
```

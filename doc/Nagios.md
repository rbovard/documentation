Nagios
======

* [Monitor web page](#monitor-web-page)

Monitor web page
----------------

```batchfile
check_http --IP-address=<ip-address> --url=http[s]://<hostname>/<path> [--ssl] --no-body --warning=<warning-time> --critical=<critical-time>
```

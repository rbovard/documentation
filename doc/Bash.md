Bash
====

* [Search](#search)
    * [Return filenames with searched text in subfolders](#return-filenames-with-searched-text-in-subfolders)
    * [Search specific words in given files](#search-specific-words-in-given-files)
    * [Find empty subfolders](#find-empty-subfolders)
    * [Find file by extension](#find-file-by-extension)
* [Packages](#packages)
    * [Update and upgrade](#update-and-upgrade)
    * [Check if a package is present](#check-if-a-package-is-present)
* [Logs](#logs)
    * [Display Apache logs in realtime](#display-apache-logs-in-realtime)
* [Disk](#disk)
    * [Display disk free](#display-disk-free)
    * [Display disk free inodes](#display-disk-free-inodes)
    * [Display directory usage](#display-directory-usage)
* [Restart services](#restart-services)
    * [Apache](#apache)
    * [PostgreSQL](#postgresql)
    * [Tomcat](#tomcat)
* [Proxy](#proxy)
    * [Most programs](#most-programs)
    * [apt-get and Update Manager](#advanced-packaging-tool-and-update-manager)
    * [GTK based programs](#gtk-based-programs)
    * [Git](#git)
* [Monitoring](#monitoring)
    * [Get HTTP status](#get-http-status)
* [Miscellaneous](#miscellaneous)
    * [Check OS version](#check-os-version)

Search
------

### Return filenames with searched text in subfolders

```bash
grep -lr '<word>' .
```

### Search specific words in given files

```bash
grep -n '\(<word1>\|<word2>\|<word3>\)' <path>/*.ext
```

### Find empty subfolders

```bash
find <path> -type d -empty
```

### Find file by extension

```bash
find <path> -type f -name "*.<extension>"
```

Packages
--------

### Update and upgrade

```bash
sudo apt update && sudo apt full-upgrade
```

### Check if a package is present

```bash
dpkg -l <package-name>
```

Logs
----

### Display Apache logs in realtime

```bash
tail -f /var/log/apache2/error.log
tail -f /var/log/apache2/access.log
```

Disk
----

### Display disk free

```bash
df -h
```

### Display disk free inodes

```bash
df -i
```

### Display directory usage

```bash
du -hs <path>
```

Restart services
----------------

### Apache

```bash
sudo /etc/init.d/apache2 graceful
sudo /etc/init.d/apache2 restart
```

### PostgreSQL

```bash
sudo /etc/init.d/postgresql restart
```

### Tomcat

```bash
sudo /etc/init.d/tomcat-tomcat1 restart
```

Proxy
-----

### Most programs

File `/etc/environment`

```bash
http_proxy=http://<server>:<port>/
https_proxy=http://<server>:<port>/
ftp_proxy=http://<server>:<port>/
HTTP_PROXY=http://<server>:<port>/
HTTPS_PROXY=http://<server>:<port>/
FTP_PROXY=http://<server>:<port>/
no_proxy="127.0.0.1, localhost"
```

### Advanced Packaging Tool and Update Manager

File `/etc/apt/apt.conf.d/95proxies`

```bash
Acquire::http::proxy "http://<server>:<port>/";
Acquire::ftp::proxy "http://<server>:<port>/";
Acquire::https::proxy "http://<server>:<port>/";
```

### GTK based programs

```bash
gsettings set org.gnome.system.proxy mode "manual"
gsettings set org.gnome.system.proxy.http host "<server>"
gsettings set org.gnome.system.proxy.http port <port>
gsettings set org.gnome.system.proxy.ftp host "<server>"
gsettings set org.gnome.system.proxy.ftp port <port>
gsettings set org.gnome.system.proxy.https host "<server>"
gsettings set org.gnome.system.proxy.https port <port>
```

### Git

```bash
git config --global url."https://".insteadOf git://
```

Monitoring
----------

### Get HTTP status

```bash
curl -Is <url> | head -n 1
```

Miscellaneous
-------------

### Check OS version

```bash
lsb_release -a
```

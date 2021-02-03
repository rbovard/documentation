# Bash

* [Files](#files)
    * [Symlink content of directory](symlink-content-of-directory)
    * [Create new file with content](create-new-file-with-content)
* [Search](#search)
    * [Return filenames with searched text in subfolders](#return-filenames-with-searched-text-in-subfolders)
    * [Search specific words in given files](#search-specific-words-in-given-files)
    * [Find empty subfolders](#find-empty-subfolders)
    * [Find file by extension](#find-file-by-extension)
    * [Count files in subfolders](#count-files-in-subfolders)
    * [Filter unique grep results](#filter-unique-grep-results)
    * [Search latest occurences](#search-latest-occurences)
    * [Search in compressed file](#search-in-compressed-file)
* [Security](#security)
    * [Change recursively permissions and group inside a folder](change-recursively-permissions-and-group-inside-a-folder)
    * [Change recursively permissions and group inside a folder excluding some files](change-recursively-permissions-and-group-inside-a-folder-excluding-some-files)
* [Packages](#packages)
    * [Install a package](#install-a-package)
    * [Update and upgrade](#update-and-upgrade)
    * [Clean cache](#clean-cache)
    * [Check if a package is present](#check-if-a-package-is-present)
    * [Search in packages list](#search-in-packages-list)
    * [Add key](#add-key)
    * [Uninstall a package](#uninstall-a-package)    
* [Logs](#logs)
    * [Display Apache logs in realtime](#display-apache-logs-in-realtime)
* [Disk](#disk)
    * [Display disk free](#display-disk-free)
    * [Display disk free inodes](#display-disk-free-inodes)
    * [Display directory usage](#display-directory-usage)
    * [Display subdirectories usage](#display-subdirectories-usage)
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
    * [Pass HTTP Referer in URL](#pass-http-referer-in-url)
    * [Get current public IP](#get-current-public-ip)

## Files

### Symlink content of directory

```bash
cp --symbolic-link /path/to/source/* /path/to/destination
```

### Create new file with content

```bash
echo '<text>' > <file>
```

Use `>>` to append text to existing file

## Search

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

### Count files in subfolders

```bash
ls -lR | egrep -c '^-'
```

### Filter unique grep results

```bash
grep <word> <file> | sort | uniq
```

### Search latest occurences

```bash
tac <file> | grep -m 10 '<word>'
```

### Search in compressed file

```bash
zgrep '<word>' <file>
```

## Security

### Change recursively permissions and group inside a folder

```bash
chmod -R <octal> <path>
chgrp -R <group> <path>
```

### Change recursively permissions and group inside a folder excluding some files

`'.?*'` for hidden files

```bash
find <path> \( -name '.?*' -o -name '*.<extension>' \) -prune -o -exec chmod <octal> {} +
find <path> \( -name '.?*' -o -name '*.<extension>' \) -prune -o -exec chgrp <group> {} +
```

## Packages

### Install a package

```bash
sudo apt install <package>
```

### Update and upgrade

```bash
sudo apt update && sudo apt full-upgrade
```

### Clean cache

```bash
sudo apt clean
```

### Search in packages list

```bash
apt search <value>
```

### Check if a package is present

```bash
dpkg -l <package>
```

### Uninstall a package

```
sudo apt purge <package>
sudo apt autoremove
```

### Add key

```bash
curl --silent <url>.key | sudo apt-key add -
```

## Logs

### Display Apache logs in realtime

```bash
tail -f /var/log/apache2/error.log
tail -f /var/log/apache2/access.log
```

## Disk

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

### Display subdirectories usage

Ordered by size

```bash
du -h --max-depth=1 <path> | sort -hr
```

## Restart services

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

## Proxy

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

## Monitoring

### Get HTTP status

```bash
curl -Is <url> | head -n 1
```

## Miscellaneous

### Check OS version

```bash
lsb_release -a
```

### Pass HTTP Referer in URL

```bash
curl --referer <referer> "<url>"
```

### Get current public IP

```bash
curl ipinfo.io/ip
```

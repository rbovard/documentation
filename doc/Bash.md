Bash
====

* [grep](#grep)
    * [Return filenames with searched text in subfolders](#return-filenames-with-searched-text-in-subfolders)
    * [Search specific words in given files](#search-specific-words-in-given-files)
* [dpkg](#dpkg)
    * [Check if a package is present](#check-if-a-package-is-present)
* [find](#find)
    * [Find empty subfolders](#find-empty-subfolders)
* [tail](#tail)
    * [Display Apache logs in realtime](#display-apache-logs-in-realtime)
* [df](#df)
    * [Display disk free](#display-disk-free)
    * [Display disk free inodes](#display-disk-free-inodes)
* [du](#du)
    * [Display directory usage](#display-directory-usage)
* [Restart services](#restart-services)
    * [Apache](#apache)
    * [PostgreSQL](#postgresql)
    * [Tomcat](#tomcat)

grep
----

### Return filenames with searched text in subfolders

```bash
grep -lr '<word>' .
```

### Search specific words in given files

```bash
grep -n '\(<word1>\|<word2>\|<word3>\)' <path>/*.ext
```

dpkg
----

### Check if a package is present

```bash
dpkg -l <package-name>
```

find
----

### Find empty subfolders

```bash
find <path> -type d -empty
```

tail
----

### Display Apache logs in realtime

```bash
tail -f /var/log/apache2/error.log
tail -f /var/log/apache2/access.log
```

df
--

### Display disk free

```bash
df -h
```

### Display disk free inodes

```bash
df -i
```

du
--

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

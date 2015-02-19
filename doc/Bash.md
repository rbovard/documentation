Bash
====

* [grep](#grep)
* [dpkg](#dpkg)
* [find](#find)
* [tail](#tail)
* [df](#df)
* [du](#du)
* [Restart services](#restart-services)

grep
----

```bash
# Return filenames with searched text in subfolders
grep -lr '<word>' .

# Search specific words in given files
grep -n '\(<word1>\|<word2>\|<word3>\)' <path>/*.ext
```

dpkg
----

```bash
# Check if a package is present
dpkg -l <package-name>
```

find
----

```bash
# Find empty subfolders
find <path> -type d -empty
```

tail
----

```bash
# Display Apache logs in realtime
tail -f /var/log/apache2/error.log
tail -f /var/log/apache2/access.log
```

df
--

```bash
# Display disk free
df -h

# Display disk free inodes
df -i
```

du
--

```bash
# Display directory usage
du -hs <path>
```

Restart services
----------------

```bash
# Apache
sudo /etc/init.d/apache2 graceful
sudo /etc/init.d/apache2 restart

# PostgreSQL
sudo /etc/init.d/postgresql restart

# Tomcat
sudo /etc/init.d/tomcat-tomcat1 restart
```

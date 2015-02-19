Bash
====

* [grep](#grep)
* [dpkg](#dpkg)
* [find](#find)

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

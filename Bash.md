Bash
====

grep
----

```bash
# Return filenames with searched text in subfolders
grep -lr 'word1' .

# Search specific words in given files
grep -n '\(word1\|word2\|word3\)' folder/*.ext
```

dpkg
----

```bash
# Check if a package is present
dpkg -l package-name
```


Git
===

Configuration
-------------

```bash
[color]
    diff = auto
    status = auto
    branch = auto
[core]
    pager = less -r
```

Branches
--------

```bash
# Create new branch
git checkout master
git fetch origin
git pull origin master
git push origin origin:refs/heads/branch
git checkout -b branch origin/branch

# Merge branch
git checkout master
git merge branch
git push origin master
git branch -d branch
git push origin :branch
```

reset
-----

Undo the last commit (not pushed)

```bash
git reset HEAD^
```

Remove all local changes (not committed)

```bash
git reset --hard
```

commit
------

Edit last commit message (not pushed)

```bash
git commit --amend -m 'New commit message'
```

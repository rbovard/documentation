Git
===

* [Configuration](#configuration)
* [Branch](#branch)
* [Reset](#reset)
* [Commit](#commit)
* [Fork](#fork)
* [Submodule](#submodule)

Configuration
-------------

File `~/.gitconfig`

```bash
[color]
    diff = auto
    status = auto
    branch = auto
[core]
    pager = less -r
```

Branch
------

```bash
# Create new branch
git checkout master
git fetch origin
git pull origin master
git push origin origin:refs/heads/<branch>
git checkout -b <branch> origin/<branch>

# Resolve conflicts (if any)
git fetch origin
git merge master
vim <conflict_file>
git add <conflict_file>
git commit -m 'Resolve conflicts'

# Merge branch
git checkout master
git merge <branch>
git push origin master
git branch -d <branch>
git push origin :<branch>
```

Reset
-----

```bash
# Undo the last commit (not pushed)
git reset HEAD^

# Remove all local changes (not committed)
git reset --hard
```

Commit
------

```bash
# Edit last commit message (not pushed)
git commit --amend -m '<new-message>'
```

Fork
----

```bash
# Syncing a fork
git checkout master
git fetch upstream
git merge upstream/master
git push origin master
```

Submodule
---------

```bash
# Update submodules
git submodule sync
git submodule update --init
git submodule foreach git submodule sync
git submodule foreach git submodule update --init
```

Git
===

* [Configuration](#configuration)
* [Branch](#branch)
    * [Create new branch](#create-new-branch)
    * [Resolve conflicts (if any)](#resolve-conflicts-if-any)
    * [Merge branch](#merge-branch)
* [Reset](#reset)
    * [Undo the last commit (not pushed)](#undo-the-last-commit-not-pushed)
    * [Remove all local changes (not committed)](#remove-all-local-changes-not-committed)
* [Commit](#commit)
    * [Edit last commit message (not pushed)](#edit-last-commit-message-not-pushed)
* [Fork](#fork)
    * [Syncing a fork](#syncing-a-fork)
* [Submodule](#submodule)
    * [Update submodules](#update-submodules)

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

### Create new branch

```bash
git checkout master
git fetch origin
git pull origin master
git push origin origin:refs/heads/<branch>
git checkout -b <branch> origin/<branch>
```

### Resolve conflicts (if any)

```bash
git checkout <branch>
git fetch origin
git merge master
vim <conflict_file>
git add <conflict_file>
git commit -m 'Resolve conflicts'
```

### Merge branch

```bash
git checkout master
git merge <branch>
git push origin master
git branch -d <branch>
git push origin :<branch>
```

Reset
-----

### Undo the last commit (not pushed)

```bash
git reset HEAD^
```

### Remove all local changes (not committed)

```bash
git reset --hard
```

Commit
------

### Edit last commit message (not pushed)

```bash
git commit --amend -m '<new-message>'
```

Fork
----

### Syncing a fork

```bash
git checkout master
git fetch upstream
git merge upstream/master
git push origin master
```

Submodule
---------

### Update submodules

```bash
git submodule sync
git submodule update --init
git submodule foreach git submodule sync
git submodule foreach git submodule update --init
```

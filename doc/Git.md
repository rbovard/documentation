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
    * [Edit last commit message (not pushed)](#edit-last-commit-message-not-pushed)
* [Update](#update)
    * [Syncing a fork](#syncing-a-fork)
    * [Update submodules](#update-submodules)
* [Rebase](#rebase)
    * [Squash commits](#squash-commits)
    * [Edit commit](#edit-commit)
    * [Rebase branch onto master](#rebase-branch-onto-master)

Configuration
-------------

File `~/.gitconfig`

```bash
[color]
    diff = auto
    status = auto
    branch = auto
[core]
    editor = vim
    pager = less -r

[credential]
    helper = cache --timeout=3600
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

### Edit last commit message (not pushed)

```bash
git commit --amend -m '<new-message>'
```

Update
------

### Syncing a fork

```bash
git checkout master
git fetch upstream
git merge upstream/master
git push origin master
```

If error `fatal: 'upstream' does not appear to be a git repository`

```bash
git remote -v
git remote add upstream <upstream-url>
```

### Update submodules

```bash
git submodule sync
git submodule update --init
git submodule foreach git submodule sync
git submodule foreach git submodule update --init
```

Rebase
------

### Squash commits

Rebase

```bash
git log
git rebase -i HEAD~<n>
```

With `<n>` last commits

Commands

* `p, pick = use commit`
* `r, reword = use commit, but edit the commit message`
* `f, fixup = use commit, but meld into previous commit and discard this commit's log message`

Push rebase

```bash
git push -f origin <branch>
```

### Edit commit

```bash
git rebase --interactive <hash>^
```

Modify `pick` to `edit`

Make changes

```bash
git commit --all --amend --no-edit
git rebase --continue
git push -f origin <branch>
```

### Rebase branch onto master

```bash
git fetch upstream
git rebase upstream/master
git status
vim <conflict_file>
git add <conflict_file>
git rebase --continue
git push -f origin <branch>
```

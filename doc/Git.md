# Git

* [Configuration](#configuration)
* [Clone](#clone)
* [Branch](#branch)
    * [Create new branch](#create-new-branch)
    * [Rebase branch onto master (if necessary)](#rebase-branch-onto-master-if-necessary)
    * [Merge branch](#merge-branch)
    * [Checkout a branch from another fork](#checkout-a-branch-from-another-fork)
* [Reset](#reset)
    * [Remove all local changes (not committed)](#remove-all-local-changes-not-committed)
    * [Undo the last commit (not pushed)](#undo-the-last-commit-not-pushed)
    * [Edit last commit message (not pushed)](#edit-last-commit-message-not-pushed)
    * [Revert a commit](#revert-a-commit)
* [Update](#update)
    * [Syncing a fork](#syncing-a-fork)
    * [Update submodules](#update-submodules)
* [Rebase](#rebase)
    * [Squash commits](#squash-commits)
    * [Edit commit](#edit-commit)
    * [Rebase onto other branch](#rebase-onto-other-branch)
* [Cherry pick](#cherry-pick)
    * [Cherry pick commit](#cherry-pick-commit)
* [Stash](#stash)
    * [Move uncommitted changes to a new branch](#move-uncommitted-changes-to-a-new-branch)
    * [Save temporarily changes](#save-temporarily-changes)
    * [List stashes](#list-stashes)
    * [Load specific stash](#load-specific-stash)
* [Search](#search)
    * [Search in repository files](#search-in-repository-files)
    * [Search files in repositorys](#search-files-in-repository)
* [Tag](#tag)
    * [List all tags](#list-all-tags)
    * [Checkout a tagged version](#checkout-a-tagged-version)

## Configuration

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

## Clone

```bash
git clone <url>
```

## Branch

### Create new branch

```bash
git checkout master
git pull
git checkout -b <branch>
```

#### From an existing distant branch

```bash
git checkout master
git pull
git checkout <branch>
```

#### Based on another local branch

```bash
git checkout master
git pull
git checkout -b <branch> <existing-branch>
```

### Rebase branch onto master (if necessary)

```bash
git checkout master
git pull
git checkout <branch>
git rebase master
git status
vim <conflict_file>
git add <conflict_file>
git rebase --continue
git push -f origin <branch>
```

If error `fatal: 'upstream' does not appear to be a git repository`

```bash
git remote -v
git remote add upstream <upstream-url>
```

### Merge branch

```bash
git checkout master
git merge <branch>
git push origin master
git branch -d <branch>
git push origin :<branch>
```

#### Into an existing branch

```bash
git checkout <existing-branch>
git merge --no-ff <branch>
git push origin <existing-branch>
git branch -d <branch>
git push origin :<branch>
```

#### From a fork

```bash
git checkout master
git merge <branch>
git push upstream master
git branch -d <branch>
git push origin :<branch>
git push origin master
```

### Checkout a branch from another fork

```
git remote add <username> https://github.com/<username>/<repository>
git fetch <username>
git checkout -b <branch> <username>/<branch>
```

## Reset

### Remove all local changes (not committed)

```bash
git reset --hard
```

### Undo the last commit (not pushed)

```bash
git reset HEAD^
```

### Edit last commit message (not pushed)

```bash
git commit --amend -m '<new-message>'
```

### Come back at previous state (commits not pushed)

```bash
git log
# Search commit and copy its hash
git reset --hard <hash>
```

### Revert a commit

```bash
git log
# Search commit and copy its hash
git revert --no-edit <hash>
```

## Update

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

## Rebase

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
git rebase -i <hash>^
```

Modify `pick` to `edit`

Make changes

```bash
git commit --all --amend --no-edit
git rebase --continue
git push -f origin <branch>
```

### Rebase onto other branch

```bash
git fetch upstream
git rebase -i upstream/<other-branch>
```

Remove all `pick` expect the ones to commit

```bash
git push -f origin <branch>
```

## Cherry pick

### Cherry pick commit

```bash
git cherry-pick <SHA>
```

## Stash

### Move uncommitted changes to a new branch

```bash
git stash
git stash branch <branch> stash@{0}
git commit -am '<message>'
git push -u origin <branch>
```

### Save temporarily changes

```
git stash
```

### List stashes

```
git stash list
```

### Load specific stash

```
git stash pop stash@{<stash-index>}
```

## Search

### Search in repository files

```bash
git grep -n '<value>'
```

### Search files in repository

```bash
git ls-files | grep <filename>
```

## Tag

### List all tags

```bash
git tag -l
```

### Checkout a tagged version

```bash
git checkout tags/<tag>
```

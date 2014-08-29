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

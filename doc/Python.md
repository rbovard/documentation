# Python

* [Virtual environments](#virtual-environments)
  * [Create a virtual environment](#create-a-virtual-environment)
  * [Activate a virtual environment](#activate-a-virtual-environment)
* [Packages installer](#packages-installer)
  * [Install a package](#install-a-package)
  * [Upgrade a package](#upgrade-a-package)
  * [Uninstall a package](#uninstall-a-package)
  * [Create a requirements file](#create-a-requirements-file)
* Scripts
  * [Copy folder](../code/python/copy_folder.py)

## Virtual environments

### Create a virtual environment

```
python -m venv <path\to\venv>
```

### Activate a virtual environment

```
cd <venv>
.\Scripts\Activate.ps1
```

## Packages installer

### Install a package

```
pip install <package>
pip install <package>==1.0.4
pip install -r requirements.txt
```

### Upgrade a package

```
pip install --upgrade <package>
```

### Uninstall a package

```
pip uninstall <package>
```

With its dependencies:

```
pip-autoremove <package> -y
```

*Need `pip-autoremove` package installed*

### Create a requirements file

```
pip freeze > requirements.txt
```

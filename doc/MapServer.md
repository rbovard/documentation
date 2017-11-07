MapServer
=========

* [Optimization](#optimization)
    * [Layer](#layer)
    * [Projection](#projection)
    * [Simple comparison](#simple-comparison)
    * [List expressions](#list-expressions)
* [Miscellaneous](#miscellaneous)
    * [Get MapServer version](#get-mapserver-version)

Optimization
------------

### Layer

Define those parameters for each layer:

* `EXTENT`: To avoid to compute it on the fly
* `MAXSCALEDENOM`: To avoid to render data at all scales

### Projection

Remove all unneeded projection definitions from the EPSG database (`CONFIG "PROJ_LIB" "/path/to/epsg"`) to avoid to lookup all defintions at each query.

### Simple comparison

Use string comparison instead of regular expression comparison:

```
CLASSITEM "foo"
CLASS
    EXPRESSION "bar"
```

Instead of:

```
EXPRESSION ("[foo]" = "bar")
```

### List expressions

Use list expressions to compare a string attribute to a list of multiple possible values instead of regex or mapserver expressions:

```
EXPRESSION {motorway,trunk}
```

Instead of:

```
# Regex expression
EXPRESSION /motorway|trunk/

# MapServer expression
EXPRESSION ("[roadtype]" IN "motorway,trunk")
```

Miscellaneous
-------------

### Get mapserver version

```bash
/usr/lib/cgi-bin/mapserv -v
```

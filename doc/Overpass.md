# Overpass

* [Overpass QL](#overpass-ql)
    * [Points in a geographical area](#points-in-a-geographical-area)
    * [With attribute filter](#with-attribute-filter)
* [Attribute filters](#attribute-filters)
* [Overpass Turbo shortcuts](#overpass-turbo-shortcuts)
    * [Current map view](#current-map-view)
    * [Geographical search](#geographical-search)
    * [Recently modified](#recently-modified)
    * [Last modified by user](#last-modified-by-user)
* [Display ways](#display-ways)
    * [As point](#as-point)
    * [As area](#as-area)
    * [Union of nodes and ways as point](#union-of-nodes-and-ways-as-point)
* [Multiple queries](#multiple-queries)
    * [Combination of values](#combination-of-values)
    * [Combination of attributes](#combination-of-attributes)

## Overpass QL

### Points in a geographical area

```
node(46.777, 6.653, 46.79, 6.66);
out;
```

### With attribute filter

```
node["emergency"="defibrillator"](46.777, 6.653, 46.79, 6.66);
out;
```

## Attribute filters

- `["key"]`: Objects with this key and any value
- `[!"key"]`: Objects without this key and any value
- `["key"="value"]`: Objects with this key and this value
- `["key"!="value"]`: Objects with this key without this value
- `["key"~"value"]`: Objects with this key and a value corresponding to this regular expression
- `["key"!~"value"]`: Objects with this key and a value not match this regular expression

## Overpass Turbo shortcuts

### Current map view

```
node["emergency"="defibrillator"]({{bbox}});
out;
```

### Geographical search

Based on Nominatim

```
{{geocodeArea:"Yverdon-les-Bains"}}->.searchArea;
node["emergency"="defibrillator"](area.searchArea);
out;
```

### Recently modified

```
node["emergency"="defibrillator"](newer:"{{date:1 month}}")({{bbox}});
out;
```

### Last modified by user

```
node["emergency"="defibrillator"](user:"<username>")({{bbox}});
out;
```

## Display ways

### As point

```
way["amenity"="restaurant"]({{bbox}});
out center;
```

### As area

```
way["amenity"="restaurant"]({{bbox}});
(._;>;);
out;
```

### Union of nodes and ways as point

```
[bbox:{{bbox}}];
(
  node["amenity"="restaurant"];
  way["amenity"="restaurant"];
);
out center;
```

## Multiple queries

### Combination of values

```
node["amenity"~"restaurant|bar"]({{bbox}});
out;
```

### Combination of attributes

`~` because several values are possible

```
node["amenity"="restaurant"]["cuisine"~"italian"]({{bbox}});
out;
```

# Overpass

## Overpass QL

### Points in a geographical area

```
node(46.777, 6.653, 46.79, 6.66);
out;
```

### With attribute filter

```
node`["emergency"="defibrillator"]`(46.777, 6.653, 46.79, 6.66);
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
node["amenity"="bar"](area.searchArea);
out;
```

## Display ways

### As centroid

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

### Union of nodes and ways

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

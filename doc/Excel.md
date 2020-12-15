# Excel

* [Split string on character](#split-string-on-character)

## Split string on character

### Before

```
=GAUCHE(<column>; TROUVE("<character>"; <column>) - 1)
```

### After

```
=DROITE(<column>; NBCAR(<column>) - TROUVE("<character>"; <column>))
```

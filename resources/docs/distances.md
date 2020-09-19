## Examples using Distances

### Importing the library:

```
>>> from siarnaq.distances import Distance
```

### List of the supported scales:

```
>>> Degree().scales
{'mi', 'km'}
```

- *km for Kilometer*

- *mi for mile*

### Using the conversions methods:

```
>>> Distance.conv_km_to_mi(1)
0.6215040397762586

>>> Distance.conv_mi_to_km(1)
1.609
```

### Creating a Distance object:

- *Create a Distance object with its default values (scale=\'km\' and dist=0)*:

```
>>> d = Distance()
``` 

- *Create a Distance object in the Kilometer scale and a distance of 10.*

```
>>> d = Distance(dist=10)
```

- *Create a Distance object in the Mile scale and a distance of 0.*

```
>>> d = Distance(scale='mi')
```

- *Creates a Distance object in the Mile scale and a distance of 10.*

```
>>> d = Degree(scale='fa', dist=32)
```

### Properties:

#### Getting properties

```
>>> distance = Distance(scale='mi', dist=1)

>>> distance
Distance('mi', 1.0)

>>> distance.scale
'mi'

>>> distance.dist
1.0

>>> distance.mile
1.0

>>> distance.kilometer
1.609
```

#### Setting properties

```
>>> distance = Distance(scale='mi', dist=1)

>>> distance
Distance('mi', 1.0)

>>> distance.scale = 'km'

>>> distance
Distance('km', 1.609)
```

### Representing the Distance object:

Both str() and repr() methods are implemented:

```
>>> str(Distance())
'0.0 km'

>>> repr(Distance())
"Distance('km', 0.0)"

>>> Distance()
Distance('km', 0.0)
```

### Distances Arithmetic

```
>>> d1 = Distance(scale='km', dist=1)
>>> d2 = Distance(scale='mi', dist=1)

>>> d = d1 + d2
>>> d
Distance('km', 2.609)

>>> d = d1 - d2
>>> d
Distance('km', -0.609)

>>> d = d2 + d1
>>> d
Distance('mi', 1.6215040397762586)

>>> d = d1 + d1
>>> d
Distance('km', 2.0)

>>> d = d1 + 2
>>> d
Distance('km', 3.0)

>>> d += 1
>>> d
Distance('km', 4.0)

>>> d *= 2
>>> d
Distance('km', 8.0)

>>> d /= 2
>>> d
Distance('km', 4.0)
```
## Examples using Degrees

### Importing the library:

```
>>> from siarnaq.degrees import Degree
```

### List of the supported scales:

```
>>> Degree().scales
{'ce', 'fa', 'ke', 'ra'}
```

- *ce for Celcius*

- *fa for Fahrenheit*

- *ke for Kelvin*

- *ra for Rankine*

### Using the conversions methods:

```
>>> Degree.conv_ce_to_fa(0)
32.0

>>> Degree.conv_ce_to_ke(0)
273.15

>>> Degree.conv_ce_to_ra(0)
491.67

>>> Degree.conv_fa_to_ce(32)
-17.77777777777778

>>> Degree.conv_fa_to_ke(0)
255.3722222222222

>>> Degree.conv_fa_to_ra(0)
459.67

>>> Degree.conv_ke_to_ce(0)
-273.15

>>> Degree.conv_ke_to_fa(0)
-459.67

>>> Degree.conv_ke_to_ra(0)
0.0

>>> Degree.conv_ra_to_ce(0)
-273.15

>>> Degree.conv_ra_to_fa(0)
-459.67

>>> Degree.conv_ra_to_ke(0)
0.0
```

### Creating a Degree object:

- *Create a Degree object with its default values (scale=\'ce\' and temp=0)*:

```
>>> d = Degree()
``` 

- *Create a Degree object in the Celcius scale and a temperature of 10 degrees.*

```
>>> d = Degree(temp=10)
```

- *Create a Degree object in the Kelvin scale and a temperature of 0 degrees.*

```
>>> d = Degree(scale='ke')
```

- *Creates a Degree object in the Fahrenheit scale and a temperature of 32 degrees.*

```
>>> d = Degree(scale='fa', temp=32)
```

### Properties:

#### Getting properties

```
>>> temperature = Degree('fa', 10.0)

>>> temperature.scale
'fa'

>>> temperature.temp
10.0

>>> temperature.celcius
-12.222222222222221

>>> temperature.fahrenheit
10.0

>>> temperature.kelvin
260.92777777777775

>>> temperature.rankine
469.67
```

#### Setting properties

```
>>> temperature = Degree('ce', 10.0)

>>> temperature
Degree('ce', 10.0)

>>> temperature.scale = 'ke'

>>> temperature
Degree('ke', 283.15)
```

### Representing the Degree object:

Both str() and repr() methods are implemented:

```
>>> str(Degree())
'0.0 °C'

>>> repr(Degree(scale='ra', temp=0))
"Degree('ra', 0.0)"

>>> Degree(scale='ke', temp=0)
Degree('ke', 0.0)
```

### Degrees Arithmetic

```
>>> t1 = Degree('ce', 10)
>>> t2 = Degree('fa', 10)

>>> t = t1 + t2
>>> t
Degree('ce', -2.2222222222222214)

>>> t = t1 - t2
>>> t
Degree('ce', 22.22222222222222)

>>> t = t1 + 5
>>> t
Degree('ce', 15.0)

>>> t = t1 - 5
>>> t
Degree('ce', 5.0)

>>> t += 0.5
>>> t
Degree('ce', 5.5)

>>> t *= 1.5
>>> t
Degree('ce', 8.25)

>>> t /= 2
>>> t
Degree('ce', 4.125)
```
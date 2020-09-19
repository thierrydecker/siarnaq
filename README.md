# Siarnaq project

## What is this name?

> **Siarnaq**, also designated Saturn **XXIX**, is a prograde irregular 
> satellite of Saturn. It was discovered at the Mauna Kea Observatory by 
> astronomers Brett Gladman and John Kavelaars in 2000, and given the 
> temporary designation **S/2000 S 3**. Named after Siarnaq, the Inuit goddess
> of the sea, it is the largest member of the Inuit group of irregula.
>
> From Wikipedia, the free encyclopedia

## The project

Siarnaq project aims to become a library dedicated to units conversions.

## Available conversions

### Degrees

The *Degree* class currently supports the following scales :

- Celcius
- Fahrenheit
- Kelvin
- Rankine

### Distances

The *Distance* class currently supports the following scales :

- Kilometer
- Mile

## Installation

The library is available on Pypi and can be installed via: 

```pip install siarnaq```

## Testing

The test are written with pytest and can be run as follow:

```pytest tests/ -v```

or

```python -m pytest tests/ -v```

We try to maintain a high level of testing coverage...

## Usage examples

[Degrees examples](resources/docs/degrees.md)

[Distances examples](resources/docs/distances.md)
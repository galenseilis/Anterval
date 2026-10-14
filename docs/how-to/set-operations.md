# Set Operations

Anterval provides standard set-theoretic operations on intervals.

## Intersection

Returns the intersection of two intervals, or `None` if they do not overlap (considering boundary openness).

```python
from anterval import Interval

a = Interval(0, 10)  # [0, 10)
b = Interval(5, 15)  # [5, 15)
print(a.intersection(b))  # [5, 10)
```

Touching at a closed boundary results in a point intersection:

```python
a = Interval(0, 1, left_closed=True, right_closed=True)  # [0,1]
b = Interval(1, 2, left_closed=True, right_closed=True)  # [1,2]
print(a.intersection(b))  # [1,1] (point interval)
```

Touching at open boundaries gives no intersection:

```python
a = Interval(0, 1, left_closed=False, right_closed=False)  # (0,1)
b = Interval(1, 2, left_closed=False, right_closed=False)  # (1,2)
print(a.intersection(b))  # None
```

## Union

Returns the union if intervals overlap or are contiguous (touch at a boundary where at least one is closed). Otherwise returns `None`.

```python
a = Interval(0, 10)
b = Interval(5, 15)
print(a.union(b))  # [0, 15)
```

Contiguous intervals (touching at a closed boundary) can be unioned:

```python
a = Interval(0, 1, right_closed=True)  # [0,1]
b = Interval(1, 2, left_closed=True)  # [1,2]
print(a.union(b))  # [0,2]
```

## Difference

Returns a list of intervals representing `self \ other` (elements in self but not in other).

```python
a = Interval(0, 10)  # [0,10)
b = Interval(3, 7)  # [3,7)
print(a.difference(b))  # [[0,3), [7,10)]
```

Removing from the middle can produce 0, 1, or 2 intervals:

```python
a = Interval(0, 10)
b = Interval(0, 5)  # remove prefix
print(a.difference(b))  # [[5,10)]

c = Interval(0, 10)
d = Interval(5, 10)  # remove suffix
print(c.difference(d))  # [[0,5)]

e = Interval(0, 10)
f = Interval(0, 10)  # remove everything
print(e.difference(f))  # []
```

## Complement

Returns the complement of an interval within a universe. The universe is treated as a closed interval `[universe_start, universe_end]`.

```python
a = Interval(2, 4)
complement = a.complement(0, 10)  # complement in [0,10]
print(complement)  # [[0,2), [4,10]]
```

If the universe is invalid (start >= end), a `ValueError` is raised.

```python
try:
    Interval(1, 2).complement(5, 5)
except ValueError as e:
    print(e)
```

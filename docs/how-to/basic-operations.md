# Basic Operations

## Checking for Overlap and Containment

### Testing Membership

```python
from anterval import Interval

interval = Interval(1, 10)
print(interval.contains(5))  # True
print(5 in interval)  # True
```

### Comparing Intervals

Intervals support rich comparisons (lexicographic ordering based on start, end, left_closed, right_closed):

```python
a = Interval(1, 5)
b = Interval(1, 10)
c = Interval(2, 5)

print(a < b)  # True (end differs)
print(a < c)  # True (start differs)
print(a == Interval(1, 5))  # True
```

Intervals are hashable and can be used in sets/dicts:

```python
items = {Interval(1, 2), Interval(1, 2), Interval(3, 4)}
print(len(items))  # 2
```

## Arithmetic Operations

### Addition (Minkowski Sum)

Adding two intervals gives their Minkowski sum, with boundary closedness being the AND of the corresponding boundaries:

```python
a = Interval(1, 3, True, True)  # [1,3]
b = Interval(2, 4, True, True)  # [2,4]
c = a + b
print(c)  # [3,7]
print(c.left_closed, c.right_closed)  # True, True
```

For half-open intervals:

```python
a = Interval(1, 3, True, False)  # [1,3)
b = Interval(2, 4, False, True)  # (2,4]
print(a + b)  # (3,7)
```

### Multiplication

Multiplication is not implemented for general intervals:

```python
a = Interval(1, 2)
b = Interval(3, 4)
try:
    a * b
except NotImplementedError:
    print("Not implemented")
```

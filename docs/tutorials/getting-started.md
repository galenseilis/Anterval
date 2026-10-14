# Getting Started with Anterval

This tutorial will walk you through the basics of working with intervals using Anterval.

## Creating Intervals

An interval is defined by its start and end points, along with whether each boundary is open or closed.

```python
from anterval import Interval

# Default: closed on left, open on right: [start, end)
interval = Interval(1, 5)
print(interval)  # [1, 5)
```

### Boundary Configurations

You can control boundary openness independently:

```python
# Both closed: [1, 5]
closed = Interval(1, 5, left_closed=True, right_closed=True)

# Both open: (1, 5)
open_ = Interval(1, 5, left_closed=False, right_closed=False)

# Left open, right closed: (1, 5]
mixed = Interval(1, 5, left_closed=False, right_closed=True)
```

## Membership Testing

Use `contains()` or the `in` operator to check if a value falls within an interval:

```python
interval = Interval(1, 5)  # [1, 5)

print(interval.contains(1))  # True
print(1 in interval)  # True (same as contains)
print(4 in interval)  # True
print(5 in interval)  # False (open on right)
print(0 in interval)  # False
```

For point intervals (where start equals end), only a fully closed point interval contains that value:

```python
point = Interval(3, 3, left_closed=True, right_closed=True)
print(3 in point)  # True

empty_like = Interval(3, 3)  # [3, 3) is effectively empty
print(3 in empty_like)  # False
```

## Working with Different Types

Anterval works with any type that supports ordering (totally ordered):

```python
# Strings (lexicographic order)
s_interval = Interval("a", "c")
print("b" in s_interval)  # True
print("c" in s_interval)  # False

# Datetimes
from datetime import datetime

start = datetime(2023, 1, 1)
end = datetime(2023, 12, 31)
year = Interval(start, end)
print(datetime(2023, 6, 15) in year)  # True
```

## Next Steps

Now that you understand the basics, check out the [How-To Guides](../how-to/basic-operations.md) for more advanced operations!

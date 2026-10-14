# Anterval

Abstract interval class for arbitrary totally ordered types.

![Anterval logo](logo.png)

## Overview

Anterval is a Python library providing generic interval types that work with any totally ordered domain (numbers, strings, datetimes, etc.). It supports configurable open/closed boundaries, set operations (intersection, union, difference, complement), arithmetic operations, and property-based testing helpers.

## Quick Start

```python
from anterval import Interval

# Half-open interval [1, 3) by default
interval = Interval(1, 3)
print(interval)  # [1, 3)
print(1 in interval)  # True
print(3 in interval)  # False

# Closed interval
closed = Interval(1, 3, left_closed=True, right_closed=True)
print(3 in closed)  # True

# Set operations
a = Interval(0, 10)
b = Interval(5, 15)
print(a.intersection(b))  # [5, 10)
print(a.union(b))  # [0, 15)
```

## Installation

```bash
pip install anterval
# or
uv add anterval
```

## Features

- Generic over any totally ordered type
- Configurable boundary openness (open/closed on left and right)
- Set operations: contains, intersection, union, difference, complement
- Rich comparison operators (`<`, `<=`, `==`, `>=`, `>`)
- Hashable for use in sets and dicts
- Membership testing with `in`
- Property-based testing strategies for Hypothesis
- Comprehensive API design following Python conventions

## License

Apache-2.0

# Property-Based Testing with Hypothesis

Anterval provides Hypothesis strategies for generating intervals of common types, useful for writing property-based tests.

## Available Strategies

The strategies are available in `anterval.testing.hypothesis.strategies`:

```python
from anterval.testing.hypothesis.strategies import (
    datetime_intervals,
    float_intervals,
    int_intervals,
    text_intervals,
)
```

## Usage Example

```python
from hypothesis import given

from anterval import Interval
from anterval.testing.hypothesis.strategies import int_intervals


@given(int_intervals())
def test_intersection_commutative(interval_a: Interval, interval_b: Interval):
    assert interval_a.intersection(interval_b) == interval_b.intersection(interval_a)


@given(int_intervals())
def test_contains_endpoints(interval: Interval):
    assert interval.contains(interval.start) == interval.left_closed
    assert interval.contains(interval.end) == interval.right_closed
```

## Customizing Strategies

Each strategy generates intervals with appropriate bounds for the type:

- `int_intervals()`: Generates intervals over integers
- `float_intervals()`: Generates intervals over floats
- `text_intervals()`: Generates intervals over strings (lexicographic)
- `datetime_intervals()`: Generates intervals over datetimes

You can combine these with other Hypothesis strategies to add constraints as needed. Let us know if you need custom strategies for your domain types!

# Interval Semantics

## Boundary Semantics

Intervals in Anterval are parameterized by openness/closedness of both boundaries. This allows representing half-open intervals (common in programming, e.g., `[start, end)`) and fully closed/open intervals as needed.

- **Left-closed** `[start, ...)`: The left endpoint `start` is included in the interval.
- **Left-open** `(start, ...)`: The left endpoint `start` is excluded from the interval.
- **Right-closed** `(..., end]`: The right endpoint `end` is included in the interval.
- **Right-open** `(..., end)`: The right endpoint `end` is excluded from the interval.

By default, intervals are `[start, end)` (left-closed, right-open), which is a common choice for ranges over discrete types.

## Empty and Degenerate Intervals

A degenerate interval where `start == end` is non-empty only if both boundaries are closed: `[x, x]` contains the single point `x`. If either boundary is open when `start == end`, the interval is empty and contains nothing.

## Set-Theoretic Operations

Operations follow standard mathematical set theory for intervals, but must account for boundary openness:

- **Intersection**: A point on the boundary is included only if *both* intervals include that boundary.
- **Union**: Two intervals union if they overlap or are *contiguous*. They are contiguous if they touch at the same boundary value and at least one of them is closed at that touching boundary (allowing the boundary to be included in the union).
- **Difference**: Returns zero, one, or two intervals as a result.
- **Complement**: Defined relative to a universe interval. The complement is calculated as `universe \ self`.

## Ordering

Intervals are totally ordered lexicographically by `(start, end, left_closed, right_closed)`. This provides a consistent ordering useful for sorting and use as dict keys, independent of the specific semantics of the contained type beyond its total ordering.

## Generality

The implementation is generic over any type `T` that supports comparison (`<`, `==`, etc.). This includes numbers, strings, datetimes, and any user-defined types with total ordering. Interval arithmetic (`+`) works when the underlying type supports the corresponding operations.

"""Core interval types for the :mod:`anterval` package."""

from __future__ import annotations

from typing import Final, override

__all__: Final[list[str]] = ["Interval"]


class Interval[T]:
    """An interval with configurable open/closed boundaries.

    By default the interval is closed on the left and open on the right, i.e.
    ``[start, end)``. Both boundaries may be inverted independently.
    """

    def __init__(
        self,
        start: T,
        end: T,
        left_closed: bool = True,
        right_closed: bool = False,
    ) -> None:
        """Initializes the Interval.

        Args:
            start: Start of the interval.
            end: End of the interval.
            left_closed: True if the interval is closed on the left, False otherwise.
            right_closed: True if the interval is closed on the right, False otherwise.

        Raises:
            ValueError: If the interval boundaries are invalid.

        """
        if end < start:
            raise ValueError("Interval end must not be less than interval start.")

        self.start: T = start
        self.end: T = end
        self.left_closed: bool = left_closed
        self.right_closed: bool = right_closed

    @override
    def __repr__(self) -> str:
        """String representation of the interval."""
        left_bracket = "[" if self.left_closed else "("
        right_bracket = "]" if self.right_closed else ")"
        return f"{left_bracket}{self.start}, {self.end}{right_bracket}"

    def contains(self, value: T) -> bool:
        """Checks if a given value is within the interval.

        Args:
            value: The value to check.

        Returns:
            bool: True if the value is within the interval, False otherwise.

        """
        left_check: bool = value > self.start or (
            self.left_closed and value == self.start
        )
        right_check: bool = value < self.end or (
            self.right_closed and value == self.end
        )
        return left_check and right_check

    def intersection(self, other: Interval[T]) -> Interval[T] | None:
        """Returns the intersection of this interval with another.

        Args:
            other: The other interval.

        Returns:
            The intersection interval, or ``None`` if they do not overlap.

        """
        if self._is_empty() or other._is_empty():
            return None
        if self.end < other.start or (
            self.end == other.start and not (self.right_closed and other.left_closed)
        ):
            return None
        if other.end < self.start or (
            other.end == self.start and not (other.right_closed and self.left_closed)
        ):
            return None

        new_start_val = max(self.start, other.start)
        new_end_val = min(self.end, other.end)

        # Intersection requires both to be closed at a common boundary for the
        # boundary point to be included.
        if new_start_val == self.start and new_start_val == other.start:
            new_start_closed = self.left_closed and other.left_closed
        elif new_start_val == self.start:
            new_start_closed = self.left_closed
        else:
            new_start_closed = other.left_closed

        if new_end_val == self.end and new_end_val == other.end:
            new_end_closed = self.right_closed and other.right_closed
        elif new_end_val == self.end:
            new_end_closed = self.right_closed
        else:
            new_end_closed = other.right_closed

        if new_start_val > new_end_val:
            return None
        if new_start_val == new_end_val and not (new_start_closed and new_end_closed):
            return None
        return Interval(new_start_val, new_end_val, new_start_closed, new_end_closed)

    def _is_empty(self) -> bool:
        return self.start > self.end or (
            self.start == self.end and not (self.left_closed and self.right_closed)
        )

    def _unionable(self, other: Interval[T]) -> bool:
        """Return True when the intervals overlap or touch at a closed boundary."""
        return not (
            self.end < other.start
            or (
                self.end == other.start and not (self.right_closed or other.left_closed)
            )
            or other.end < self.start
            or (
                other.end == self.start and not (other.right_closed or self.left_closed)
            )
        )

    def union(self, other: Interval[T]) -> Interval[T] | None:
        """Return the union if this interval overlaps or is contiguous with another.

        Args:
            other: The other interval.

        Returns:
            The union interval, or ``None`` if they do not overlap.

        """
        if self._is_empty():
            return other if not other._is_empty() else None
        if other._is_empty():
            return self
        if not self._unionable(other):
            return None

        # Compare using ordering of start/end with closedness for boundary decisions
        new_start_val = min(self.start, other.start)
        new_end_val = max(self.end, other.end)

        # Determine closedness at boundaries by taking the more inclusive (True wins)
        if new_start_val == self.start and new_start_val == other.start:
            new_start_closed = self.left_closed or other.left_closed
        elif new_start_val == self.start:
            new_start_closed = self.left_closed
        else:
            new_start_closed = other.left_closed

        if new_end_val == self.end and new_end_val == other.end:
            new_end_closed = self.right_closed or other.right_closed
        elif new_end_val == self.end:
            new_end_closed = self.right_closed
        else:
            new_end_closed = other.right_closed

        return Interval(new_start_val, new_end_val, new_start_closed, new_end_closed)

    def difference(self, other: Interval[T]) -> list[Interval[T]]:
        """Returns the difference of this interval with another.

        Args:
            other: The other interval.

        Returns:
            list[Interval[T]]: A list of intervals after subtracting the other interval.

        """
        if self._is_empty():
            return []
        if other._is_empty():
            return [self]
        if other.start > self.end or (
            other.start == self.end and not (other.left_closed and self.right_closed)
        ):
            # No overlap
            return [self]
        if other.end < self.start or (
            other.end == self.start and not (other.right_closed and self.left_closed)
        ):
            # No overlap
            return [self]

        intervals: list[Interval[T]] = []
        if other.start > self.start or (
            other.start == self.start and not other.left_closed
        ):
            intervals.append(
                Interval(
                    self.start,
                    other.start,
                    self.left_closed,
                    not other.left_closed,
                ),
            )
        if other.end < self.end or (other.end == self.end and not other.right_closed):
            intervals.append(
                Interval(
                    other.end,
                    self.end,
                    not other.right_closed,
                    self.right_closed,
                ),
            )
        return [
            i
            for i in intervals
            if not (i.end < i.start)
            and not (i.end == i.start and not (i.left_closed and i.right_closed))
        ]

    def complement(self, universe_start: T, universe_end: T) -> list[Interval[T]]:
        """Returns the complement of this interval within a specified universe.

        Args:
            universe_start: Start of the universe.
            universe_end: End of the universe.

        Returns:
            list[Interval[T]]: A list of intervals representing the complement.

        Raises:
            ValueError: If the universe boundaries are invalid.

        """
        if universe_start >= universe_end:
            raise ValueError("Universe start must be before universe end.")

        universe = Interval(
            start=universe_start,
            end=universe_end,
            left_closed=True,
            right_closed=True,
        )
        return universe.difference(self)

    def _ordering_key(self) -> tuple[T, T, bool, bool]:
        return (self.start, self.end, self.left_closed, self.right_closed)

    def __lt__(self, other: object) -> bool:
        """Lexicographic ordering of intervals."""
        if not isinstance(other, Interval):
            return NotImplemented
        return self._ordering_key() < other._ordering_key()

    def __le__(self, other: object) -> bool:
        """Lexicographic ordering of intervals."""
        if not isinstance(other, Interval):
            return NotImplemented
        return self._ordering_key() <= other._ordering_key()

    def __gt__(self, other: object) -> bool:
        """Lexicographic ordering of intervals."""
        if not isinstance(other, Interval):
            return NotImplemented
        return self._ordering_key() > other._ordering_key()

    def __ge__(self, other: object) -> bool:
        """Lexicographic ordering of intervals."""
        if not isinstance(other, Interval):
            return NotImplemented
        return self._ordering_key() >= other._ordering_key()

    @override
    def __eq__(self, other: object) -> bool:
        """Two intervals are equal when all four components are equal."""
        if not isinstance(other, Interval):
            return NotImplemented
        return self._ordering_key() == other._ordering_key()

    def __hash__(self) -> int:
        """Intervals hash consistently with equality."""
        return hash(self._ordering_key())

    def __contains__(self, value: T) -> bool:
        """Support the ``value in interval`` membership operator."""
        return self.contains(value)

    def __add__(self, other: Interval[T]) -> Interval[T]:
        """Return the Minkowski sum of two intervals."""
        return Interval(
            start=self.start + other.start,
            end=self.end + other.end,
            left_closed=self.left_closed and other.left_closed,
            right_closed=self.right_closed and other.right_closed,
        )

    def __mul__(self, other: Interval[T]) -> Interval[T]:
        """Return the product of two intervals (not implemented)."""
        raise NotImplementedError

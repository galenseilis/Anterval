"""Shared helpers for interval tests."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from anterval import Interval


def boundary_points(interval: Interval[int]) -> list[int]:
    """Return sample points around an interval's boundaries.

    The points cover the two endpoints, their immediate neighbours, the
    midpoint and one point just outside each end. They are used to verify
    set-like operations on a finite sample instead of the whole (possibly
    unbounded) domain.
    """
    return [
        interval.start - 1,
        interval.start,
        interval.start + 1,
        (interval.start + interval.end) // 2,
        interval.end - 1,
        interval.end,
        interval.end + 1,
    ]


def sample_points(*intervals: Interval[int]) -> list[int]:
    """Return a sorted, de-duplicated set of boundary sample points."""
    points: set[int] = set()
    for interval in intervals:
        points.update(boundary_points(interval))
    return sorted(points)

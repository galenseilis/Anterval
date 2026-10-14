"""Hypothesis strategies producing intervals of common ordered types."""

from __future__ import annotations

from typing import TYPE_CHECKING

from hypothesis import strategies as st

from anterval import Interval

if TYPE_CHECKING:
    from datetime import datetime


@st.composite
def float_intervals(draw: st.DrawFn) -> Interval[float]:
    """Generates intervals of floats."""
    n1 = draw(st.floats())
    n2 = draw(st.floats())
    start = min(n1, n2)
    end = max(n1, n2)
    left_closed = draw(st.booleans())
    right_closed = draw(st.booleans())
    return Interval(
        start=start,
        end=end,
        left_closed=left_closed,
        right_closed=right_closed,
    )


@st.composite
def int_intervals(draw: st.DrawFn) -> Interval[int]:
    """Generates intervals of integers."""
    n1 = draw(st.integers())
    n2 = draw(st.integers(min_value=n1))
    left_closed = draw(st.booleans())
    right_closed = draw(st.booleans())
    return Interval(
        start=n1,
        end=n2,
        left_closed=left_closed,
        right_closed=right_closed,
    )


@st.composite
def text_intervals(draw: st.DrawFn) -> Interval[str]:
    """Generate intervals of text."""
    n1 = draw(st.text())
    n2 = draw(st.text())
    start = min(n1, n2)
    end = max(n1, n2)
    left_closed = draw(st.booleans())
    right_closed = draw(st.booleans())
    return Interval(
        start=start,
        end=end,
        left_closed=left_closed,
        right_closed=right_closed,
    )


@st.composite
def datetime_intervals(draw: st.DrawFn) -> Interval[datetime]:
    """Generate intervals of datetimes."""
    n1 = draw(st.datetimes())
    n2 = draw(st.datetimes())
    start = min(n1, n2)
    end = max(n1, n2)
    left_closed = draw(st.booleans())
    right_closed = draw(st.booleans())
    return Interval(
        start=start,
        end=end,
        left_closed=left_closed,
        right_closed=right_closed,
    )

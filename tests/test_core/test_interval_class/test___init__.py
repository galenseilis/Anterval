import math

from hypothesis import given, strategies as st

from anterval import Interval


@given(
    a=st.integers(),
    b=st.integers(),
    left_closed=st.booleans(),
    right_closed=st.booleans(),
)
def test_integers(a: int, b: int, left_closed: bool, right_closed: bool) -> None:
    assert isinstance(a, int)
    assert isinstance(b, int)
    assert isinstance(left_closed, bool)
    assert isinstance(right_closed, bool)
    start = min(a, b)
    end = max(a, b)
    assert isinstance(start, int)
    assert isinstance(end, int)
    assert start <= end
    interval = Interval(
        start=start, end=end, left_closed=left_closed, right_closed=right_closed
    )
    assert isinstance(interval.start, int)
    assert isinstance(interval.end, int)
    assert isinstance(interval.left_closed, bool)
    assert isinstance(interval.right_closed, bool)
    assert interval.start == start
    assert interval.end == end
    assert interval.left_closed == left_closed
    assert interval.right_closed == right_closed
    assert interval.start <= interval.end


@given(
    a=st.floats(),
    b=st.floats(),
    left_closed=st.booleans(),
    right_closed=st.booleans(),
)
def test_floats(a: float, b: float, left_closed: bool, right_closed: bool) -> None:
    assert isinstance(a, float)
    assert isinstance(b, float)
    assert isinstance(left_closed, bool)
    assert isinstance(right_closed, bool)
    start = min(a, b)
    end = max(a, b)
    assert isinstance(start, float)
    assert isinstance(end, float)
    assert start <= end
    interval = Interval(
        start=start, end=end, left_closed=left_closed, right_closed=right_closed
    )
    assert isinstance(interval.start, float)
    assert isinstance(interval.end, float)
    assert (interval.start == start) or (
        math.isnan(interval.start) and math.isnan(start)
    )
    assert (interval.end == end) or (math.isnan(interval.end) and math.isnan(end))
    assert interval.left_closed == left_closed
    assert interval.right_closed == right_closed
    assert (interval.start <= interval.end) or (
        math.isnan(interval.end) and math.isnan(end)
    )


@given(
    a=st.text(),
    b=st.text(),
    left_closed=st.booleans(),
    right_closed=st.booleans(),
)
def test_text(a: str, b: str, left_closed: bool, right_closed: bool) -> None:
    assert isinstance(a, str)
    assert isinstance(b, str)
    assert isinstance(left_closed, bool)
    assert isinstance(right_closed, bool)

    start = min(a, b)
    end = max(a, b)

    assert isinstance(start, str)
    assert isinstance(end, str)
    assert start <= end

    interval = Interval(
        start=start, end=end, left_closed=left_closed, right_closed=right_closed
    )
    assert interval.start == start
    assert interval.end == end
    assert interval.start <= interval.end
    assert interval.left_closed == left_closed
    assert interval.right_closed == right_closed
    assert interval.start <= interval.end

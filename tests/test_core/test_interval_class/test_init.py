from hypothesis import given, strategies as st

from anterval import Interval

@given(
    a=st.integers(),
    b=st.integers(),
    left_closed=st.booleans(),
    right_closed=st.booleans(),
)
def test_integers(a: int, b: int, left_closed: bool, right_closed: bool) -> None:
    start = min(a, b)
    end = max(a, b)
    assert isinstance(start, int)
    assert isinstance(end, int)
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
    start = min(a, b)
    end = max(a, b)
    interval = Interval(
        start=start, end=end, left_closed=left_closed, right_closed=right_closed
    )
    assert isinstance(interval.start, float)
    assert isinstance(interval.end, float)
    assert (interval.start == start) or (interval.start == float('nan'))
    assert (interval.end == end) or (interval.end == float('nan'))
    assert interval.left_closed == left_closed
    assert interval.right_closed == right_closed
    assert interval.start <= interval.end

@given(
    a=st.text(),
    b=st.text(),
    left_closed=st.booleans(),
    right_closed=st.booleans(),
)
def test_text(a: str, b: str, left_closed: bool, right_closed: bool) -> None:
    start = min(a, b)
    end = max(a, b)
    interval = Interval(
        start=start, end=end, left_closed=left_closed, right_closed=right_closed
    )
    assert interval.start == start
    assert interval.end == end
    assert interval.left_closed == left_closed
    assert interval.right_closed == right_closed
    assert interval.start <= interval.end

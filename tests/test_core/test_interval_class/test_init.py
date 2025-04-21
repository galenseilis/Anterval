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
    interval = Interval(
        start=start, end=end, left_closed=left_closed, right_closed=right_closed
    )


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

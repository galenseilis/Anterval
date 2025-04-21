from hypothesis import given, strategies as st

from anterval import Interval


@given(
    a=st.integers(),
    b=st.integers(),
    left_closed=st.booleans(),
    right_closed=st.booleans(),
)
def test_int(a, b, left_closed, right_closed):
    start = min(a, b)
    end = max(a, b)
    interval = Interval(
        start=start, end=end, left_closed=left_closed, right_closed=right_closed
    )
    assert 1 != 2

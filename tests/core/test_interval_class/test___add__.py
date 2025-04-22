import math

from hypothesis import given
from hypothesis import strategies as st

from anterval import Interval


@given(
    a=st.floats(),
    b=st.floats(),
    left_closed=st.booleans(),
    right_closed=st.booleans(),
)
def test_floats(a: float, b: float, left_closed: bool, right_closed: bool) -> None:
    """Test if Interval initializes with floats correctly."""
    assert isinstance(a, float)
    assert isinstance(b, float)
    assert isinstance(left_closed, bool)
    assert isinstance(right_closed, bool)

    start = min(a, b)
    end = max(a, b)
    assert isinstance(start, float)
    assert isinstance(end, float)
    assert (start <= end) or (math.isnan(start) or math.isnan(end))

    # Check that interval is correctly initialized.
    interval = Interval(
        start=start, end=end, left_closed=left_closed, right_closed=right_closed,
    )

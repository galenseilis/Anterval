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
    """Test if Interval represents with floats correctly."""
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

    result = repr(interval)

    left_bracket = "[" if left_closed else "("
    right_bracket = "]" if right_closed else ")"
    expected = f"{left_bracket}{start}, {end}{right_bracket}"

    assert result == expected


@given(
    a=st.integers(),
    b=st.integers(),
    left_closed=st.booleans(),
    right_closed=st.booleans(),
)
def test_integers(a: int, b: int, left_closed: bool, right_closed: bool) -> None:
    """Test if Interval represents with integers correctly."""
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
        start=start, end=end, left_closed=left_closed, right_closed=right_closed,
    )

    result = repr(interval)

    left_bracket = "[" if left_closed else "("
    right_bracket = "]" if right_closed else ")"
    expected = f"{left_bracket}{start}, {end}{right_bracket}"

    assert result == expected


@given(
    a=st.text(),
    b=st.text(),
    left_closed=st.booleans(),
    right_closed=st.booleans(),
)
def test_text(a: str, b: str, left_closed: bool, right_closed: bool) -> None:
    """Test if Interval represents with strings correctly."""
    # Check that test input data is correct.
    assert isinstance(a, str)
    assert isinstance(b, str)
    assert isinstance(left_closed, bool)
    assert isinstance(right_closed, bool)

    # Check that input is correct.
    start = min(a, b)
    end = max(a, b)

    assert isinstance(start, str)
    assert isinstance(end, str)
    assert start <= end

    # Check that interval is correctly initialized.
    interval = Interval(
        start=start, end=end, left_closed=left_closed, right_closed=right_closed,
    )

    result = repr(interval)

    left_bracket = "[" if left_closed else "("
    right_bracket = "]" if right_closed else ")"
    expected = f"{left_bracket}{start}, {end}{right_bracket}"

    assert result == expected

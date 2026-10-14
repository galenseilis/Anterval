from __future__ import annotations

from hypothesis import given
from hypothesis import strategies as st

from anterval import Interval
from anterval.testing.hypothesis.strategies import int_intervals


def test_minkowski_sum_of_closed_intervals() -> None:
    result = Interval(1, 2, True, True) + Interval(3, 4, True, True)
    assert result == Interval(4, 6, True, True)


def test_minkowski_sum_of_open_intervals() -> None:
    result = Interval(1, 2, False, False) + Interval(3, 4, False, False)
    assert result == Interval(4, 6, False, False)


def test_minkowski_sum_of_half_open_intervals() -> None:
    result = Interval(1, 2, True, False) + Interval(3, 4, False, True)
    assert result == Interval(4, 6, False, False)


def test_sum_of_point_and_interval() -> None:
    point = Interval(10, 10, True, True)
    result = point + Interval(1, 3, False, False)
    assert result == Interval(11, 13, False, False)


@st.composite
def _nonnegative_int_intervals(draw: st.DrawFn) -> Interval[int]:
    start = draw(st.integers(min_value=0, max_value=10_000))
    end = draw(st.integers(min_value=start, max_value=10_000))
    return Interval(
        start=start,
        end=end,
        left_closed=draw(st.booleans()),
        right_closed=draw(st.booleans()),
    )


@given(_nonnegative_int_intervals(), _nonnegative_int_intervals())
def test_sum_components(a: Interval, b: Interval) -> None:
    result = a + b
    assert result.start == a.start + b.start
    assert result.end == a.end + b.end
    assert result.left_closed == (a.left_closed and b.left_closed)
    assert result.right_closed == (a.right_closed and b.right_closed)


@given(int_intervals(), int_intervals())
def test_sum_commutes(a: Interval, b: Interval) -> None:
    assert a + b == b + a

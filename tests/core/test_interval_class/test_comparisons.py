import pytest
from hypothesis import given

from anterval import Interval
from anterval.testing.hypothesis.strategies import int_intervals


def test_start_dominates_ordering() -> None:
    assert Interval(0, 10) < Interval(1, 10)
    assert Interval(1, 10) > Interval(0, 10)


def test_end_breaks_ties_on_start() -> None:
    assert Interval(1, 2) < Interval(1, 3)


def test_closedness_is_tie_breaker() -> None:
    open_interval = Interval(1, 2, left_closed=False, right_closed=False)
    closed_interval = Interval(1, 2, left_closed=True, right_closed=True)
    assert open_interval < closed_interval


def test_total_order_relations() -> None:
    a = Interval(1, 2)
    b = Interval(1, 3)
    assert a < b
    assert a <= b
    assert b > a
    assert b >= a
    assert a >= a
    assert a <= a


def test_equality_implies_ordering_equality() -> None:
    a = Interval(1, 2)
    assert not (a < a)
    assert a <= a
    assert a >= a


def test_comparing_with_non_interval_raises() -> None:
    with pytest.raises(TypeError):
        Interval(1, 2) < 5
    with pytest.raises(TypeError):
        Interval(1, 2) >= "x"


@given(int_intervals(), int_intervals())
def test_ordering_matches_tuple_order(a: Interval, b: Interval) -> None:
    def key(interval: Interval):
        return (
            interval.start,
            interval.end,
            interval.left_closed,
            interval.right_closed,
        )

    assert (a < b) == (key(a) < key(b))
    assert (a <= b) == (key(a) <= key(b))
    assert (a > b) == (key(a) > key(b))
    assert (a >= b) == (key(a) >= key(b))

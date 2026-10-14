from hypothesis import given

from anterval import Interval
from anterval.testing.hypothesis.strategies import int_intervals
from tests.helpers import sample_points


def test_overlapping_intervals() -> None:
    assert Interval(0, 10).intersection(Interval(5, 15)) == Interval(5, 10)


def test_fully_contained() -> None:
    assert Interval(0, 10).intersection(Interval(3, 4)) == Interval(3, 4)


def test_identical() -> None:
    interval = Interval(0, 10)
    assert interval.intersection(interval) == interval


def test_disjoint_returns_none() -> None:
    assert Interval(0, 1).intersection(Interval(2, 3)) is None


def test_touching_with_both_closed_returns_point() -> None:
    left = Interval(0, 1, left_closed=True, right_closed=True)
    right = Interval(1, 2, left_closed=True, right_closed=True)
    assert left.intersection(right) == Interval(1, 1, True, True)


def test_touching_with_one_open_returns_none() -> None:
    left = Interval(0, 1, left_closed=True, right_closed=False)
    right = Interval(1, 2, left_closed=True, right_closed=True)
    assert left.intersection(right) is None


def test_touching_with_both_open_returns_none() -> None:
    left = Interval(0, 1, left_closed=False, right_closed=False)
    right = Interval(1, 2, left_closed=False, right_closed=False)
    assert left.intersection(right) is None


def test_closedness_preserved_on_lower_bound() -> None:
    open_interval = Interval(0, 10, left_closed=False, right_closed=False)
    closed_interval = Interval(0, 5, left_closed=True, right_closed=True)
    result = open_interval.intersection(closed_interval)
    assert result is not None
    # At the shared left boundary both must be closed for the result to be closed.
    assert result.left_closed == (
        open_interval.left_closed and closed_interval.left_closed
    )


@given(int_intervals(), int_intervals())
def test_commutative(a: Interval, b: Interval) -> None:
    assert a.intersection(b) == b.intersection(a)


@given(int_intervals(), int_intervals())
def test_is_subset_of_both_arguments(a: Interval, b: Interval) -> None:
    result = a.intersection(b)
    if result is None:
        return
    assert result.start >= a.start
    assert result.end <= a.end
    assert result.start >= b.start
    assert result.end <= b.end


@given(int_intervals(), int_intervals())
def test_membership_is_set_intersection(a: Interval, b: Interval) -> None:
    result = a.intersection(b)
    for point in sample_points(a, b):
        in_result = result is not None and result.contains(point)
        assert in_result == (a.contains(point) and b.contains(point))

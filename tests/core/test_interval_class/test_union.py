from hypothesis import given

from anterval import Interval
from anterval.testing.hypothesis.strategies import int_intervals
from tests.helpers import sample_points


def test_overlapping_union() -> None:
    assert Interval(0, 10).union(Interval(5, 15)) == Interval(0, 15)


def test_contiguous_closed_union() -> None:
    left = Interval(0, 1, left_closed=False, right_closed=True)
    right = Interval(1, 2, left_closed=True, right_closed=False)
    assert left.union(right) == Interval(0, 2, False, False)


def test_contiguous_open_returns_none() -> None:
    left = Interval(0, 1, left_closed=False, right_closed=False)
    right = Interval(1, 2, left_closed=False, right_closed=False)
    assert left.union(right) is None


def test_disjoint_returns_none() -> None:
    assert Interval(0, 1).union(Interval(2, 3)) is None


def test_identical_union_is_self() -> None:
    interval = Interval(0, 10, left_closed=False, right_closed=True)
    assert interval.union(interval) == interval


def test_openness_preserved_on_outer_boundaries() -> None:
    result = Interval(0, 5, left_closed=False, right_closed=False).union(
        Interval(5, 10, left_closed=True, right_closed=True)
    )
    assert result == Interval(0, 10, False, True)


@given(int_intervals(), int_intervals())
def test_commutative(a: Interval, b: Interval) -> None:
    assert a.union(b) == b.union(a)


@given(int_intervals(), int_intervals())
def test_membership_is_set_union(a: Interval, b: Interval) -> None:
    result = a.union(b)
    for point in sample_points(a, b):
        if result is not None:
            assert result.contains(point) == (a.contains(point) or b.contains(point))
        else:
            assert not (a.contains(point) and b.contains(point))

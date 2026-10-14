from hypothesis import given

from anterval import Interval
from anterval.testing.hypothesis.strategies import int_intervals
from tests.helpers import sample_points


def test_no_overlap_returns_self() -> None:
    assert Interval(0, 1).difference(Interval(2, 3)) == [Interval(0, 1)]


def test_no_overlap_with_touching_open_boundaries() -> None:
    left = Interval(0, 1, left_closed=True, right_closed=False)
    right = Interval(1, 2, left_closed=True, right_closed=True)
    assert left.difference(right) == [left]


def test_right_endpoint_shared_with_closed_other() -> None:
    # [1, 2] \ [2, 3] leaves only the point 1, i.e. [1, 2).
    result = Interval(1, 2, True, True).difference(Interval(2, 3, True, False))
    assert result == [Interval(1, 2, True, False)]


def test_left_endpoint_shared_with_closed_other() -> None:
    # [2, 3] \ [1, 2] leaves only (2, 3].
    result = Interval(2, 3, True, True).difference(Interval(1, 2, True, True))
    assert result == [Interval(2, 3, False, True)]


def test_removing_middle_leaves_two_pieces() -> None:
    result = Interval(0, 10).difference(Interval(4, 6))
    assert result == [Interval(0, 4), Interval(6, 10)]


def test_removing_identical_interval_leaves_nothing() -> None:
    interval = Interval(0, 10)
    assert interval.difference(interval) == []


def test_superset_removes_everything() -> None:
    assert Interval(2, 8).difference(Interval(0, 10)) == []


def test_removing_prefix() -> None:
    assert Interval(0, 10).difference(Interval(0, 4)) == [Interval(4, 10)]


def test_removing_suffix() -> None:
    assert Interval(0, 10).difference(Interval(6, 10)) == [Interval(0, 6)]


def test_removing_open_prefix_keeps_left_endpoint() -> None:
    result = Interval(0, 10).difference(Interval(0, 4, left_closed=False))
    assert result == [Interval(0, 0, True, True), Interval(4, 10)]


@given(int_intervals(), int_intervals())
def test_membership_is_set_difference(a: Interval, b: Interval) -> None:
    pieces = a.difference(b)
    for point in sample_points(a, b):
        in_b = b.contains(point)
        in_a = a.contains(point)
        in_some_piece = any(piece.contains(point) for piece in pieces)
        assert in_some_piece == (in_a and not in_b)


@given(int_intervals(), int_intervals())
def test_pieces_are_subset_of_self(a: Interval, b: Interval) -> None:
    for piece in a.difference(b):
        assert piece.start >= a.start
        assert piece.end <= a.end


@given(int_intervals())
def test_difference_with_any_other_preserves_number_of_pieces(
    interval: Interval,
) -> None:
    pieces = interval.difference(Interval(5, 10))
    assert len(pieces) in (0, 1, 2)

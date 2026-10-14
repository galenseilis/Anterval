import pytest
from hypothesis import given

from anterval import Interval
from anterval.testing.hypothesis.strategies import int_intervals
from tests.helpers import sample_points


def test_empty_universe_invalid() -> None:
    with pytest.raises(ValueError, match="Universe start must be before universe end"):
        Interval(1, 2).complement(5, 5)


def test_universe_out_of_order_invalid() -> None:
    with pytest.raises(ValueError, match="Universe start must be before universe end"):
        Interval(1, 2).complement(10, 0)


def test_middle_interval_splits_universe() -> None:
    result = Interval(2, 4).complement(0, 10)
    assert result == [
        Interval(0, 2, left_closed=True, right_closed=False),
        Interval(4, 10, left_closed=True, right_closed=True),
    ]


def test_open_left_boundary_keeps_point() -> None:
    result = Interval(2, 4, left_closed=False).complement(0, 10)
    assert result == [Interval(0, 2, True, True), Interval(4, 10, True, True)]


def test_open_right_boundary_keeps_point() -> None:
    result = Interval(2, 4, right_closed=False).complement(0, 10)
    assert result == [Interval(0, 2), Interval(4, 10, True, True)]


def test_interval_equal_to_universe_is_empty_complement() -> None:
    interval = Interval(0, 10, True, True)
    assert interval.complement(0, 10) == []


def test_interval_outside_universe_returns_full_universe() -> None:
    assert Interval(10, 20).complement(0, 5) == [Interval(0, 5, True, True)]


def test_wider_than_universe_returns_empty() -> None:
    assert Interval(0, 20).complement(2, 5) == []


def test_point_interval_complement() -> None:
    result = Interval(3, 3, True, True).complement(0, 10)
    assert result == [Interval(0, 3, True, False), Interval(3, 10, False, True)]


@given(int_intervals())
def test_complement_membership_partitions_universe(interval: Interval) -> None:
    universe = Interval(0, 100, True, True)
    pieces = interval.complement(0, 100)
    for point in sample_points(interval, universe):
        if universe.contains(point):
            in_self = interval.contains(point)
            in_pieces = any(piece.contains(point) for piece in pieces)
            assert in_self != in_pieces

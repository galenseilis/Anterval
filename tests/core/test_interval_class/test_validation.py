import pytest

from anterval import Interval


def test_start_greater_than_end_raises() -> None:
    with pytest.raises(ValueError, match="end must not be less than"):
        Interval(5, 1)


def test_equal_boundaries_are_allowed() -> None:
    assert Interval(3, 3).start == 3
    assert Interval(3, 3).end == 3


def test_valid_interval_keeps_attributes() -> None:
    interval = Interval(1, 2, left_closed=False, right_closed=True)
    assert (interval.start, interval.end) == (1, 2)
    assert (interval.left_closed, interval.right_closed) == (False, True)

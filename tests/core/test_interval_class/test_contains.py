from hypothesis import given

from anterval import Interval
from anterval.testing.hypothesis.strategies import int_intervals, text_intervals


def test_default_left_closed_right_open() -> None:
    interval = Interval(1, 3)
    assert interval.contains(1)
    assert interval.contains(2)
    assert not interval.contains(3)


def test_both_closed() -> None:
    interval = Interval(1, 3, left_closed=True, right_closed=True)
    assert interval.contains(1)
    assert interval.contains(2)
    assert interval.contains(3)


def test_both_open() -> None:
    interval = Interval(1, 3, left_closed=False, right_closed=False)
    assert not interval.contains(1)
    assert interval.contains(2)
    assert not interval.contains(3)


def test_right_closed_left_open() -> None:
    interval = Interval(1, 3, left_closed=False, right_closed=True)
    assert not interval.contains(1)
    assert interval.contains(2)
    assert interval.contains(3)


def test_membership_operator_matches_contains() -> None:
    interval = Interval(1, 3)
    for value in (-1, 0, 1, 2, 3, 4):
        assert (value in interval) == interval.contains(value)


def test_degenerate_point_interval() -> None:
    interval = Interval(5, 5, left_closed=True, right_closed=True)
    assert interval.contains(5)
    assert not interval.contains(4)
    assert not interval.contains(6)


def test_degenerate_interval_both_closed() -> None:
    interval = Interval(5, 5, left_closed=True, right_closed=True)
    assert interval.contains(5)


def test_degenerate_interval_half_open_contains_nothing_at_endpoint() -> None:
    for left_closed, right_closed in [(False, True), (True, False), (False, False)]:
        interval = Interval(5, 5, left_closed, right_closed)
        assert not interval.contains(5)


@given(int_intervals())
def test_endpoints_respect_closedness(interval: Interval) -> None:
    if interval.start == interval.end:
        assert interval.contains(interval.start) == (
            interval.left_closed and interval.right_closed
        )
        return
    assert interval.contains(interval.start) == interval.left_closed
    assert interval.contains(interval.end) == interval.right_closed


@given(text_intervals())
def test_substring_values(interval: Interval) -> None:
    if interval.start == interval.end:
        assert interval.contains(interval.start) == (
            interval.left_closed and interval.right_closed
        )
        return
    assert interval.contains(interval.start) == interval.left_closed
    assert interval.contains(interval.end) == interval.right_closed

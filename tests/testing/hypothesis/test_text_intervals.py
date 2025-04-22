from hypothesis import given
from anterval.testing.hypothesis.strategies import text_intervals
from anterval import Interval


@given(text_intervals())
def test_is_interval(interval: Interval) -> None:
    assert isinstance(interval, Interval)

@given(text_intervals())
def test_start_is_int(interval: Interval) -> None:
    assert isinstance(interval.start, str)


@given(text_intervals())
def test_end_is_int(interval: Interval) -> None:
    assert isinstance(interval.start, str)


@given(text_intervals())
def test_left_closed_is_bool(interval: Interval) -> None:
    assert isinstance(interval.left_closed, bool)


@given(text_intervals())
def test_right_closed_is_bool(interval: Interval) -> None:
    assert isinstance(interval.right_closed, bool)


@given(text_intervals())
def test_start_leq_end(interval: Interval) -> None:
    assert interval.start <= interval.end

from hypothesis import given
import datetime
from anterval.testing.hypothesis.strategies import datetime_intervals


@given(datetime_intervals())
def test_start_is_int(interval):
    assert isinstance(interval.start, datetime.datetime)


@given(datetime_intervals())
def test_end_is_int(interval):
    assert isinstance(interval.start, datetime.datetime)


@given(datetime_intervals())
def test_left_closed_is_bool(interval):
    assert isinstance(interval.left_closed, bool)


@given(datetime_intervals())
def test_right_closed_is_bool(interval):
    assert isinstance(interval.right_closed, bool)


@given(datetime_intervals())
def test_start_leq_end(interval):
    assert interval.start <= interval.end

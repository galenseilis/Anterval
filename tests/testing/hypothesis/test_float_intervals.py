import math

from hypothesis import given

from anterval.testing.hypothesis.strategies import float_intervals


@given(float_intervals())
def test_start_is_float(interval):
    assert isinstance(interval.start, float)


@given(float_intervals())
def test_end_is_float(interval):
    assert isinstance(interval.start, float)


@given(float_intervals())
def test_left_closed_is_bool(interval):
    assert isinstance(interval.left_closed, bool)


@given(float_intervals())
def test_right_closed_is_bool(interval):
    assert isinstance(interval.right_closed, bool)


@given(float_intervals())
def test_start_leq_end_or_nan(interval):
    assert (
        (interval.start <= interval.end)
        or math.isnan(interval.start)
        or math.isnan(interval.end)
    )

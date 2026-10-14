from hypothesis import given

from anterval import Interval
from anterval.testing.hypothesis.strategies import int_intervals


def test_equal_intervals() -> None:
    assert Interval(1, 2) == Interval(1, 2)


def test_different_start() -> None:
    assert Interval(1, 2) != Interval(0, 2)


def test_different_end() -> None:
    assert Interval(1, 2) != Interval(1, 3)


def test_different_left_closedness() -> None:
    assert Interval(1, 2, left_closed=False) != Interval(1, 2)


def test_different_right_closedness() -> None:
    assert Interval(1, 2, right_closed=True) != Interval(1, 2)


def test_equality_with_non_interval() -> None:
    assert Interval(1, 2) != 5
    assert Interval(1, 2) != "1, 2"
    assert Interval(1, 2) != None  # noqa: E711


def test_equality_is_symmetric() -> None:
    assert (Interval(1, 2) == Interval(1, 2)) == (Interval(1, 2) == Interval(1, 2))


@given(int_intervals(), int_intervals())
def test_equality_matches_component_equality(a: Interval, b: Interval) -> None:
    same = (
        a.start == b.start
        and a.end == b.end
        and a.left_closed == b.left_closed
        and a.right_closed == b.right_closed
    )
    assert (a == b) == same

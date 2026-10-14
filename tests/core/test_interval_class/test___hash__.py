from hypothesis import given

from anterval import Interval
from anterval.testing.hypothesis.strategies import int_intervals


def test_equal_intervals_have_equal_hashes() -> None:
    assert hash(Interval(1, 2)) == hash(Interval(1, 2))


def test_usable_in_set_and_dict() -> None:
    interval = Interval(1, 2)
    assert interval in {Interval(1, 2), Interval(3, 4)}
    assert {interval: "x"}[Interval(1, 2)] == "x"


@given(int_intervals())
def test_hash_with_same_components_is_equal(interval: Interval) -> None:
    clone = Interval(
        interval.start, interval.end, interval.left_closed, interval.right_closed
    )
    assert hash(interval) == hash(clone)

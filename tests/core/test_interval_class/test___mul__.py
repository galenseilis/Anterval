import pytest

from anterval import Interval


def test_multiplication_is_not_implemented() -> None:
    with pytest.raises(NotImplementedError):
        Interval(1, 2) * Interval(3, 4)

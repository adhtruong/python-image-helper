from pytest import raises

from image_helper import float_range, lerp


def test_float_range():
    assert [] == list(float_range(1, 0, 0.1))
    assert [0, 0.5] == list(float_range(0, 1, 0.5))
    assert [] == list(float_range(1, 0, 0.5))
    assert [1, 0.5] == list(float_range(1, 0, -0.5))
    with raises(ValueError):
        list(float_range(0, 1, 0))


def test_lerp():
    assert 1 == lerp(0.5, 0, 1, 0, 2)
    assert -1 == lerp(0.5, 0, 1, 0, -2)

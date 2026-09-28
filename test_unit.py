import pytest
from functions import summator, div, flat_generator


@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
    (2.5, 2.5, 5.0),
])
def test_summator(a, b, expected):
    assert summator(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (6, 2, 3),
    (10, 5, 2),
    (9, 3, 3),
    (1, 1, 1),
])
def test_div(a, b, expected):
    assert div(a, b) == expected


@pytest.mark.parametrize("input_data, expected", [
    (
        [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None]],
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ),
    (
        [['x'], ['y', 'z']],
        ['x', 'y', 'z']
    ),
    (
        [[], ['a'], []],
        ['a']
    ),
])
def test_flat_generator(input_data, expected):
    assert list(flat_generator(input_data)) == expected
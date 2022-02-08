# test_linearity_coordinates.py
import pytest


@pytest.mark.parametrize("tuple1, tuple2, expected", [
    [(4, 5), (2, 3), 1],
    [(7, 6), (8, 1), -5]
    ])
def test_calculate_slope(tuple1, tuple2, expected):
    from linearity_coordinates import calculate_slope
    answer = calculate_slope(tuple1, tuple2)
    assert answer == expected


@pytest.mark.parametrize("tuple1, slope, expected", [
    [(4, 5), 1, 1],
    [(7, 6), -5, 41]
    ])
def test_calculate_intercept(tuple1, slope, expected):
    from linearity_coordinates import calculate_intercept
    answer = calculate_intercept(tuple1, slope)
    assert answer == expected


@pytest.mark.parametrize("slope, intercept, x_val, expected", [
    [1, 1, 4, 5],
    [-5, 41, 7, 6]
    ])
def test_calculate_yval(slope, intercept, x_val, expected):
    from linearity_coordinates import calculate_yval
    answer = calculate_yval(slope, intercept, x_val)
    assert answer == expected

# test_unit_testing_practice.py


import pytest

@pytest.mark.parametrize("a, b", [[]])
def test_unit_testing_practice(a,b):
    a = (x1, y1)
    b = (x2, y2)


@pytest.mark.parametrize("input_HDL, expected", [
                         [70, "Normal"],
                         [45, "Borderline Low"],
                         [20, "Low"]
                        ])
def test_check_HDL_normal(input_HDL, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input_HDL)
    assert answer == expected


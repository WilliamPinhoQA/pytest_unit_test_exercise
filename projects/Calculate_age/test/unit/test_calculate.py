import math

import pytest


from projects.Calculate_age.calculate_functions import judge_leap_year, month_days


@pytest.mark.parametrize('year, expected_result', [

    (1996, True),
    (1997, False),
    (2020, True),
    (0, 'Failed! Invalid value'),
    ('W', 'Failed! Invalid value'),
    ('65386758567856', 'Failed! Invalid value'),
    (0.5, 'Failed! Invalid value'),
    (3/8, 'Failed! Invalid value'),
    (-3/8, 'Failed! Invalid value'),
    (-19, 'Failed! Invalid value'),
    (math.sqrt(3), 'Failed! Invalid value'),
    (3 ** 39.4, 'Failed! Invalid value'),
    (3 ** 39, False),
    (4 ** 40, True)


])
def test_judge_leap_year(year, expected_result):
    """
    with mock.patch.object(builtins, 'input', lambda _: 'William'):
    with mock.patch.object(builtins, 'input', lambda _: '1996'):
    https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call
    """
    current_result = judge_leap_year(year)
    assert (expected_result == current_result)


@pytest.mark.parametrize('month, leap_year, expected_result', [

    (1, True, 31),
    (3, True, 31),
    (5, True, 31),
    (7, True, 31),
    (8, True, 31),
    (10, True, 31),
    (12, True, 31),
    (2, False, 28),
    (11, False, 30),
    (2, True, 29),
    ('W',True,'Failed! Invalid value')
])
def test_monthdays(month, leap_year, expected_result):
    current_result = month_days(month, leap_year)
    assert (expected_result == current_result)

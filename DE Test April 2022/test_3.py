# The below function doesn't work correctly. It should sum all the numbers at the
# current time. For example, 01:02:03 should return 6. Improve and fix the function,
# and write unit test(s) for it. Use any testing framework you're familiar with.

from datetime import datetime
import pytest


# [TODO]: fix the function
def time_validation(time_str: str) -> bool:
    """function checks if input is valid time"""
    try:
        datetime.strptime(time_str, '%H:%M:%S')
    except:
        raise ValueError



def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    if not isinstance(time_str, str):
        raise TypeError
    time_validation(time_str)
    list_of_string_nums = time_str.split(":")
    list_of_integer_nums = [int(num) for num in list_of_string_nums]
    return sum(list_of_integer_nums)


def test_unexpected_format():
    """test to see if function returns value error if input unexpected format"""
    with pytest.raises(ValueError):
        assert sum_current_time('40:11:11')


def test_unexpected_type():
    """test to see if function returns type error if input type unexpected"""
    with pytest.raises(TypeError):
        assert sum_current_time(459999)


def test_not_valid_time():
    """test to see if function returns value error if invalid time input"""
    with pytest.raises(ValueError):
        assert sum_current_time('45:99:99')


def test_adds_correctly():
    """test to see if function returns correct sum of time"""
    assert sum_current_time('01:52:03') == 56

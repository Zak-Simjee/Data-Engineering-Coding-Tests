import pytest

from test_3 import sum_current_time

def test_base_case():
    assert sum_current_time("01:02:03") == 6

def test_not_a_str():
    with pytest.raises(TypeError) as err:
       sum_current_time(4)

    assert err.value.args[0] == "Error: please input a string representing time in HH:MM:SS format."

def test_bad_format_str():
    with pytest.raises(ValueError) as err:
        sum_current_time("10/05/33")
    
    assert err.value.args[0] == "Error: Input string not in the right format."
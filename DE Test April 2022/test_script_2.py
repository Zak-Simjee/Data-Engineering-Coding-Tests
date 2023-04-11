import pytest

from test_2 import get_court_data

def test_postcode_not_str_request():
    with pytest.raises(TypeError) as err:
        get_court_data(55)
    assert err.value.args[0] == "Error: Please input a valid postcode."

def test_postcode_not_long_enough():
    with pytest.raises(ValueError) as err:
        get_court_data("TEST")
    assert err.value.args[0] == "Error: Postcode not long enough. Please check postcode is correct."

def test_call_api(requests_mock):
    
    url = "https://courttribunalfinder.service.gov.uk/search/results.json?postcode=TEST12"

    requests_mock.get(url, status_code=200, json={"response": "success"})

    get_court_data("TEST12")

    assert requests_mock.called
    assert requests_mock.call_count == 1
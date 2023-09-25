from working import convert
import pytest
def test_format1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
def test_format2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
def test_minutes():
    assert convert("9:35 AM to 5:25 PM") == "09:35 to 17:25"
def test_12():
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
def test_pm():
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"
def test_format():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
def test_outofrange():
    with pytest.raises(ValueError):
        convert("17 AM to 25 PM")
def test_outofrange2():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")

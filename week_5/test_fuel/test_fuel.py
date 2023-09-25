from fuel import convert, gauge
import pytest
def test_convert_empty():
    assert convert("0/10") == 0
def test_convert_full():
    assert convert("10/10") == 100
def test_convert_middle():
    assert convert("5/10") == 50
def test_convert_value_error():
    with pytest.raises(ValueError):
        convert("10/5")
        convert("cat/2")
        convert("2/cat")
def test_convert_zero_error():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")
def test_gauge_99():
    assert gauge(99) == "F"
def test_gauge_100():
    assert gauge(100) == "F"
def test_gauge_0():
    assert gauge(0) == "E"
def test_gauge_50():
    assert gauge(50) == "50%"
def test_gauge_1():
    assert gauge(1) == "E"


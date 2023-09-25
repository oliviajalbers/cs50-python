from um import count
import pytest
def test_capital():
    assert count("UM") == 1
def test_yummy():
    assert count("yummy") == 0
def test_punctuation():
    assert count("Um, hello, um.") == 2

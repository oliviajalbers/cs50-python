from numb3rs import validate
def test_255():
    assert validate("255.255.255.255") == True
def test_0():
    assert validate("0.0.0.0") == True
def test_199():
    assert validate("199.0.0.0") == True
def test_256():
    assert validate("256.0.0.0") == False
def test_300():
    assert validate("300.0.0.0") == False
def test_first():
    assert validate("255.300.300.300") == False

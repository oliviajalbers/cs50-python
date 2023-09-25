from bank import value
def test_hello():
    assert value("hello") == 0
def test_capital():
    assert value("Hello") == 0
def test_hword():
    assert value("hey") == 20
def test_other():
    assert value("what's up?") == 100
def test_punctuation():
    assert value("hello!!!") == 0
def test_number():
    assert value("hello 123") == 0


from plates import is_valid
def test_too_few():
    assert is_valid("h") == False
def test_too_many():
    assert is_valid("helloworld") == False
def test_empty():
    assert is_valid("") == False
def test_first_two():
    assert is_valid("A1") == False
def test_punctuation():
    assert is_valid("Hello!") == False
def test_space():
    assert is_valid("CS 50") == False
def test_num_middle():
    assert is_valid("CS50CS") == False
def test_first_num():
    assert is_valid("CS05") == False

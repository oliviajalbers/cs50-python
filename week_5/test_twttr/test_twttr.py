from twttr import shorten
def test_general():
    assert shorten("cat") == "ct"
def test_vowels():
    assert shorten("aeiou") == ""
def test_no_input():
    assert shorten("") == ""
def test_space():
    assert shorten(" ") == " "
def test_punctuation():
    assert shorten("hello world!") == "hll wrld!"
def test_capital_vowel():
    assert shorten("ABC") == "BC"
def test_number():
    assert shorten("ABC123") == "BC123"

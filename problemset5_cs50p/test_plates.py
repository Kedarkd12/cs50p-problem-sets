from plates import is_valid

def test_len():
    assert is_valid("AAA123")==True
    assert is_valid("CS50")==True
    assert is_valid("ABCDEFG")==False
def test_start():
    assert is_valid("1ABC")==False
    assert is_valid("A1BC")==False
    assert is_valid("AA012")==False
    assert is_valid("AA123")==True
def test_end():
    assert is_valid("AA12A")==False
    assert is_valid("AA22BB")==False
def test_specialchar():
    assert is_valid("CS50!")==False
    assert is_valid("CS 50")==False


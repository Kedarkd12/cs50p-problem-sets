from numb3rs import validate

def test_char():
    assert validate("cat")==False
def test_outofrange():
    assert validate("298.250.200.257")==True
def test_missingip():
    assert validate("200.290.18")==False
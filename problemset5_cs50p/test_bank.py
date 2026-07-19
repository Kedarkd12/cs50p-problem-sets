from bank import value

def test_hello():
    assert value("hello")==0
    assert value("Hello")==0
def test_uppercase():
    assert value("HELLO")==0
    assert value("HI")==20
def test_h():
    assert value("hey")==20
    assert value("hi")==20
def test_rest():
    assert value("whatsup")==100
    assert value("whats happened")==100
from um import count

def test_prefix():
    assert count("...um,um,um,um")==4
def test_suffix():
    assert count("um,heyy")==1
def test_case():
    assert count("UM WELL UM ACTUALLY")==2
def test_bothfix():
    assert count("hello,um,hello")==1
def test_concat():
    assert count("yummy")==0
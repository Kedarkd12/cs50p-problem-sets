from twttr import shorten

def test_lowercase():
    assert shorten("Hello, world")=="Hll, wrld"
def test_uppercase():
    assert shorten("hELLO, wORLD")=="hLL, wRLD"
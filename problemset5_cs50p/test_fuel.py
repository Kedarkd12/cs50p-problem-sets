from fuel import convert
from fuel import gauge
import pytest

def test_frac():
    assert convert("1/2")==0.5
    assert convert("4/4")==1.0
def test_frac_y():
    with pytest.raises(ValueError):
        convert("1/-4")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_frac_x():
    assert convert("0/4")==0.0
    with pytest.raises(ValueError):
        convert("-1/4")
def test_frac_xy():
    with pytest.raises(ValueError):
        convert("-1/-4")
def test_gauge():
    assert gauge(0.5)=="50%"
    assert gauge(1.0)=="F"
    assert gauge(0.0)=="E"

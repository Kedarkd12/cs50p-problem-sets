from working import convert
import pytest

def test_edge():
    assert convert("12 PM to 12 AM")=="12:00 to 00:00"
    assert convert("12:59 PM to 12:01 AM")=="12:59 to 00:01"
def test_invalid():
    with pytest.raises(ValueError):
        convert("0 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:75PM")
def test_format():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("9 to 5 PM")
    
    
    
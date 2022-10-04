from operations import multiply
from operations import add
from operations import subtract

# Testing functionality of multiply function
def test_multiply():
    assert multiply(10,9) == 90

# Testing functionality of add function
def test_add():
    assert add(13,5) == 18

# Testing functionality of subtract function
def test_subtract():
    assert subtract(18,4) == 14
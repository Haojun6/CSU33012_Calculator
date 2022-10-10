from Calc import main

# Testing functionality of addition, subtraction
def test_addsub():
 assert main("9-10+2") == 1

# Testing functionality of multiplaction, addition
def test_muladd():
 assert main("10*2+5") == 25

# Testing functionality of multiplication, subtraction
def test_mulsub():
 assert main("18-2*5") == 8

# Testing functionality of all operators
def test_all():
 assert main("20-25+3*4") == 7

from calculate import calc

# Testing functionality of addition, subtraction
def test_addsub():
 assert calc("9 - 10 + 2") == 1

# Testing functionality of multiplaction, addition
def test_muladd():
 assert calc("10 * 2 + 5") == 25

# Testing functionality of multiplication, subtraction
def test_mulsub():
 assert calc("18 - 2 * 5") == 8

# Testing functionality of all operators
def test_all():
 assert calc("20 - 25 + 3 * 4") == 7

from calculator import add, subtract

def test_add_functional():
    # Verify that 2 + 3 equals 5
    assert add(2, 3) == 5

def test_subtract_functional():
    # Verify that 10 - 4 equals 6
    assert subtract(10, 4) == 6

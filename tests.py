from .calc import add

def test_add_equals_to_8():
    assert add(5, 3) == 8

def test_add_equals_to_5():
    assert add(2, 3) == 5
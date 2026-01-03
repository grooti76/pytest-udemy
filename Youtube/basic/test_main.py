from main import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5, "2+3 should equal 5"
    assert add(0, 0) == 0, "0+0 should equal 0"
    assert add(-1, 1) == 0, "-1+1 should equal 0"

def test_divide():
    assert divide(6, 2) == 3, "6/2 should equal 3"
    assert divide(5, 2) == 2.5, "5/2 should equal 2.5"
    try:
        divide(5, 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
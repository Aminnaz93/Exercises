from functions import *
import pytest



def test_add():
    assert add(5, 3) == 8, "Should be 8"
    assert add(-1, 1) == 0, "Should be 0"
    assert add(-2, -2) == -4, "Should be -4"
    assert add(0.1,0.2) == pytest.approx(0.3), "Should be 0.30000000000000004, but approximately 0.3"

def test_sub():
    assert sub(10,5) == 5, "Should be 5"
    assert sub(4,2) == 2, "Should be 2"
    assert sub(8,7) == 1, "Should be 1"

def test_mult():
    assert mult(3, 4) == 12, "Should be 12"
    assert mult(-1, 1) == -1, "Should be -1"
    assert mult(0, 5) == 0, "Should be 0"

def test_div():
    assert div(8, 2) == 4, "Should be 4"
    assert div(5, 2) == 2.5, "Should be 2.5"
    assert div(-6, 3) == -2, "Should be -2"

# Test för att undvika division med noll
with pytest.raises(ZeroDivisionError):
    div(5, 0)


if __name__ == "__main__":
    pytest.main()



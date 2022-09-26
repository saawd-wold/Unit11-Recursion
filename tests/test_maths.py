import pytest
from src.maths import factorial, gcd

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    try:
        x = factorial(1e10)
        assert False, "Expected a RecursionError (Stack Overflow) for too-large input!"
    except RecursionError as r:
        assert True

def test_gcd():
    assert gcd(10, 5) == 5
    assert gcd(30029*43889, 34649*51869 == 1)
    
    
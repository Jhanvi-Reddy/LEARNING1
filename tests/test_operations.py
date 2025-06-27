# tests/test_operations.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator.operations import add, subtract, multiply, divide

from calculator.operations import add, subtract, multiply, divide

def test_add():
    assert add(3, 2) == 5

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(8, 2) == 4

def test_divide_by_zero():
    try:
        divide(5, 0)
    except ValueError:
        assert True
    else:
        assert False

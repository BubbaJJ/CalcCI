import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Calculator import Calc


def test_add():
    assert 13 == Calc.add(5, 8)


def test_sub():
    assert 13 == Calc.sub(19, 6)


def test_mul():
    assert 39 == Calc.mul(13, 3)


def test_div():
    assert 12 == Calc.div(48, 4)


def test_power():
    assert 9 == Calc.power(3, 2)


def test_modulo():
    assert 0 == Calc.modulo(10, 2)


def test_countChars():
    assert True is Calc.countChars("KalleAnkaP")
    assert False is Calc.countChars("KalleAnka")
    assert False is Calc.countChars("KalleAnka ")

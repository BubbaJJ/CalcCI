from main import operators
from main import output_to_txt
import os


def test_operators():
    assert "Addition" == operators(1).name
    assert operators(2).name == "Subtraction"
    assert operators(6).name != "Modulus"
    assert operators.Power.value == 6


def test_output_to_txt():
    output_to_txt('test.txt', "Kalle")
    with open('test.txt', 'r') as f:
        assert f.read() == "Kalle"
    # Deletes created file to enable testing again.
    os.remove('test.txt')

from code_examples.code_snippets import simple_calculator as sc
import pytest


X_OPERAND1 = 100
X_OPERAND2 = 10


def test_perform_addition_given_operands():
    result = sc.Calculator.add(X_OPERAND1, X_OPERAND2)
    assert result == 110


def test_perform_substraction_given_operands():
    result = sc.Calculator.substract(X_OPERAND1, X_OPERAND2)
    assert result == 90


def test_perform_multiplication_given_operands():
    result = sc.Calculator.multiply(X_OPERAND1, X_OPERAND2)
    assert result == 1000


def test_perform_division_given_operands():
    result = sc.Calculator.divide(X_OPERAND1, X_OPERAND2)
    assert result == 10


def test_division_raises_ZeroDivisionError_given_divisor_as_zero():
    X_OPERAND2 = 0
    with pytest.raises(ZeroDivisionError):
        sc.Calculator.divide(X_OPERAND1, X_OPERAND2)


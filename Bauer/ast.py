"""
Abstract syntax tree for our infix notation calculator
Taken from the official RPLY documentation
"""

import typing
from rply.token import BaseBox


class Number(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self) -> typing.Union[int, float]:
        """
        Return itself, much like the I combinator from SKI combinator calculus
        """

        return self.value


class BinaryOp(BaseBox):
    """
    Take two elements and apply one operator
    """

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


class Add(BinaryOp):
    def eval(self) -> typing.Union[int, float]:
        """
        Add two numbers
        Returns:
            typing.Union[int, float]: any numeric type of an addition operation
        """

        return self.lhs.eval() + self.rhs.eval()


class Sub(BinaryOp):
    def eval(self):
        """
        Subtract two numbers
        Returns:
            typing.Union[int, float]: any numeric type of an subtraction operation
        """

        return self.lhs.eval() - self.rhs.eval()


class Mul(BinaryOp):
    def eval(self):
        """
        Multiply two numbers
        Returns:
            typing.Union[int, float]: any numeric type of an multiply operation
        """
        return self.lhs.eval() * self.rhs.eval()


class Div(BinaryOp):
    def eval(self):
        """
        Divide two numbers
        Returns:
            typing.Union[int, float]: any numeric type of an division operation
        """

        return self.lhs.eval() * self.rhs.eval()

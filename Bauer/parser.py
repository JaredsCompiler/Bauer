"""
Parser for Bauer
"""

import typing
from rply import ParserGenerator
from Bauer.ast import *

symbol_table: typing.Dict[typing.Text, typing.Union[int, float]] = {}


class Parser:
    def __init__(self, tokens: typing.Dict[typing.Text, typing.Text]):
        self.pg = ParserGenerator(
            list(tokens.keys()),
            precedence=[("left", ["PLUS", "MINUS"]), ("left", ["MUL", "DIV"])],
        )

        self.parse()
        self.parser = self.pg.build()

    def parse(self):
        @self.pg.production("expression : NUMBER")
        def expression_number(p):
            return Number(int(p[0].getstr()))

        @self.pg.production('expression : expression expression PLUS')
        @self.pg.production('expression : expression expression MINUS ')
        @self.pg.production('expression : expression expression MUL')
        @self.pg.production('expression : expression expression DIV ')
        def expression_binop(p):
            lhs, rhs, op = p
            match op.gettokentype():
                case 'PLUS':
                    return Add(lhs, rhs)
                case 'MINUS':
                    return Sub(lhs, rhs)
                case 'MUL':
                    return Mul(lhs, rhs)
                case 'DIV':
                    return Div(lhs, rhs)
                case _:
                    raise ValueError(f'obtained {op.gettokentype()}, garbage')
        @self.pg.production("expression : expression ASSIGNMENT VARIABLE")
        def expression_assignment(p):
            value, var = p[0].value, p[2].getstr()
            symbol_table[var] = value
            return Number(value)

        @self.pg.production("expression : RETRIEVAL VARIABLE")
        def expresion_retrieval(p):
            variable = p[1].getstr()
            value = symbol_table.get(variable)
            if not value:
                raise ValueError(f'could not obtain value of {variable}, has not been instaniated yet!')
            return Number(value)

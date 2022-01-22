"""
Module that contains our Lexer
"""

import typing
from rply import LexerGenerator


class Lexer:
    """
    Class to produce tokens based on a token map
    """

    def __init__(self, token_map: typing.Dict[typing.Text, typing.Text]):
        self.lexer = LexerGenerator()
        for name, token in token_map.items():
            self.lexer.add(name, token)
        self.lexer.ignore(r"\s+")
        self.lexer = self.lexer.build()

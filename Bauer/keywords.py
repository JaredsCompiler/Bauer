"""
This contains all of the keywords used in this language
AUTHOR: Jared Dyreson
INSTITUTION: California State University Fullerton
"""

from Bauer.lexer import Lexer

token_map = {
    "NUMBER": r"\d+",
    "PLUS": r"\+",
    "MINUS": r"-",
    "MUL": r"\*",
    "DIV": r"/",
    "ASSIGNMENT": r"\=",
    "VARIABLE": r"[a-zA-Z]+",
    "RETRIEVAL": r"\?"
}


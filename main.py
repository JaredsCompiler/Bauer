from Bauer.parser import Parser
from Bauer.lexer import Lexer
from Bauer.keywords import token_map

P = Parser(token_map)
lexer = Lexer(token_map).lexer

resultant  = P.parser.parse(lexer.lex('10 =variable')).eval()
resultant  = P.parser.parse(lexer.lex('?variable')).eval()
print(resultant)

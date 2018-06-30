from lexer import lex
from parser import yacc

# Build the lexer
lexer = lex.lex()

# # Test it out
# data = '''
# 3 + 4 * 10
#   + -20 *2
# '''
# Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)

# Build the parser
parser = yacc.yacc()

# parse
while True:
  try:
      s = raw_input('calc > ')
  except EOFError:
      break
  if not s: continue
  result = parser.parse(s)
  print(result)
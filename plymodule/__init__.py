from lexer import lexer
from parser import parser

# Build the lexer
# lexer = lexer.lex.lex()

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
# parser = parser.yacc.yacc()

with open('../test', 'r') as myfile:
    data=myfile.read()
# print(data)
result = parser.parse(data)
print(result)

# parse
# while True:
#   try:
#       s = raw_input('calc > ')
#   except EOFError:
#       break
#   if not s: continue
#   result = parser.parse(s)
#   print(result)
from lexer import lexer
from parser import parser

# Build the lexer
# lexer = lexer.lex.lex()

# # Test it out
data = '''
2194

IEEE TRANSACTIONS ON CONTROL SYSTEMS TECHNOLOGY, VOL. 25, NO. 6,

NOVEMBER 2017

Feedback Controllers as Financial Advisors for Low-Income Individuals

Hugo Gonzalez Villasanti and Kevin M. Passino, Fellow, IEEE

Abstract ashusahuashuashasuhasudhasudhasuda

Index
'''
# Give the lexer some input


# Build the parser
# parser = parser.yacc.yacc()

# with open('../test', 'r') as myfile:
#     data=myfile.read()

# # Tokenize
# lexer.input(data)
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)

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
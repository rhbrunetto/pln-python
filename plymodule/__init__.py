# coding=utf-8
from lexer import lexer
from parser import parser

# For testing only
import sys

# Build the lexer
# lexer = lexer.lex.lex()

# # Test it out
# data = '''
# '''
# Give the lexer some input


# Build the parser
# parser = parser.yacc.yacc()

with open('../test', 'r') as myfile:
    data=myfile.read()
# print(data)

def tokenize():
    # Tokenize
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)

def parsing():
    result = parser.parse(data)
    print(result)

if len(sys.argv) == 1: tokenize()

if sys.argv[1] == '-l':
    tokenize()
elif sys.argv[1] == '-p':
    parsing()

# parse
# while True:
#   try:
#       s = raw_input('calc > ')
#   except EOFError:
#       break
#   if not s: continue
#   result = parser.parse(s)
#   print(result)
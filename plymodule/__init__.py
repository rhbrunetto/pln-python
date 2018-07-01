# coding=utf-8
from lexer import lexer
from parser import parser

# For testing only
import sys
import os

# Build the lexer
# lexer = lexer.lex.lex()

# # Test it out
# data = '''
# '''
# Give the lexer some input

if len(sys.argv) == 1:
    print("PRECISA DE PARAMETRO PORR")
    exit(-1)


with open(sys.argv[1], 'r') as myfile:
    data=myfile.read()

# Build the parser
# parser = parser.yacc.yacc()
def tokenize(data):
    # Tokenize
    # text_file = open(index, "w")
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)
        # text_file.write(tok)
    # text_file.close()     

def parsing(data):
    # text_file = open(index, "w")
    result = parser.parse(data)
    print(result)
    # text_file.write(result)
    # text_file.close()

# os.system("ls " + "../files/*.txt > .tmpfiles")
# with open(".tmpfiles", "r") as ins:
#     files = ins.readlines()
#     for arq in files:
#         with open(arq.replace('\n', ''), 'r') as myfile:
#             data=myfile.read()
if sys.argv[2] == '-l':
    tokenize(data)
elif sys.argv[2] == '-p':
    parsing(data)
# os.system("rm .tmpfiles")

# parse
# while True:
#   try:
#       s = raw_input('calc > ')
#   except EOFError:
#       break
#   if not s: continue
#   result = parser.parse(s)
#   print(result)
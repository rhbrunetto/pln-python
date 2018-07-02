# coding=utf-8
from lexer import lexer
from parser import parser

# Tokenize
def tokenize(data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)

def parsing(data):
    text_file = open(data, "r")
    d = text_file.read()
    article = parser.parse(d)
    text_file.close()
    return article

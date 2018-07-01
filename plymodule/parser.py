# Yacc example

import ply.yacc as yacc
import data
# Get the token map from the lexer.  This is required.
from lexer import tokens
from data.article import Article

def p_article(p):
    'article : header'
    # p[0] = Article(p[1], p[2], p[3])
    print "Article rule"

def p_header_code(p):
    'header : code publication titleandauthor abstract'
    print "Header_code rule"

def p_header_pub(p):
    'header : publication code titleandauthor abstract'
    print "Header_pub rule"

def p_code(p):
    'code : YEAR'
    print "Code rule"

def p_publication(p):
    'publication : IEEE text MONTH YEAR'
    print "Publication rule"

def p_abstract(p):
    'abstract : ABSTRACT text INDEX'
    print "Abstract rule"

def p_keywords(p):
    'keywords : INDEX text INTRO'
    print "Keywords rule"

# def p_content(p):
#     'content : INTRO text REFERENCES'
#     print "Content rule"

# def p_references(p):
#     'references : REFERENCES text'
#     print "References rule"

def p_titleandauthor(p):
    'titleandauthor : text'
    print "Title and author rule"

def p_text_general(p):
    'text : GENERAL text'
    print "Text general rule"

def p_text(p):
    'text : GENERAL'
    print "Text rule"
    
# def p_titleandauthor(p):
#     'titleandauthor : '

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# while True:
#   try:
#       s = raw_input('calc > ')
#   except EOFError:
#       break
#   if not s: continue
#   result = parser.parse(s)
#   print(result)
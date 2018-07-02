# coding=utf-8
import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'IEEE',
   'ABSTRACT',
   'INDEX',
   'TERMS',
   'CHAPTER_MARK',
   'YEAR',
   'MONTH',
   'REFERENCE_B',
   'REFERENCES',
   'GENERAL'
)

# Regular expression rules for simple tokens
def t_IEEE(t):
    r'IEEE'
    return t

def t_INDEX(t):
    r'Index'
    return t

def t_TERMS(t):
    r'Terms—'
    return t

def t_ABSTRACT(t):
    r'Abstract'
    return t

def t_CHAPTER_MARK(t):
    r'\I{1,3}\.\s([A-Z]+\s)+|(\I{1,2})?V\.\s([A-Z]+\s)+'
    return t

def t_REFERENCE_B(t):
    r'\[\d+\]((.*\S\.*\n)+)'
    return t

def t_REFERENCE_L(t):
    r'\[\d+\].*\http\.+'
    return t

t_REFERENCES    = 'REFERENCES'

def t_YEAR(t):
    r'\d{4}'
    t.value = int(t.value)    
    return t

def t_MONTH(t):
    r'JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER'
    t.value = str.lower(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
# General text
t_GENERAL = r'.*\S.*'

# Error handling rule
def t_error(t):
    # print("Illegal character '%s'" % t.value[0], t.lineno)
    t.lexer.skip(1)

# # Build the lexer
lexer = lex.lex()
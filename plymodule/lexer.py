import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'IEEE',
   'ABSTRACT',
   'INDEX',
   'CAPSTEXT',
   'VIRGULA',
   'YEAR',
   'MONTH',
   'INTRO',
   'REFERENCES',
   'GENERAL'
)

# Regular expression rules for simple tokens
t_IEEE          = 'IEEE'
t_ABSTRACT      = 'Abstract'
t_INDEX         = 'Index'
t_INTRO         = 'I. Introduction'
t_REFERENCES    = 'References'
t_VIRGULA       = ','
t_CAPSTEXT      = r'[A-Z]+|\\s+'

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

t_GENERAL = r'.*\S.*'

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# # Build the lexer
lexer = lex.lex()

# # Test it out
# data = '''
# 3 + 4 * 10
#   + -20 *2
# '''
# # Give the lexer some input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break      # No more input
#     print(tok)
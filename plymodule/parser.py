import ply.yacc as yacc
import data
# Get the token map from the lexer.  This is required.
from lexer import tokens
from data.article import Article
from data.header import Header
from data.content import Content
from data.chapter import Chapter
from data.reference import Reference

def p_article(p):
    'article : header content references'
    p[0] = Article(p[1], p[2], p[3])
    # print "Article rule"
    p[0].show()

def p_header_code(p):
    'header : code publication titleandauthor abstract keywords'
    # print "Header_code rule"
    p[0] = Header(p[2], p[1], p[3], p[4], p[5])
    # p[0].show()

def p_header_pub(p):
    'header : publication code titleandauthor abstract keywords'
    # print "Header_pub rule"
    p[0] = Header(p[1], p[2], p[3], p[4], p[5])
    # p[0].show()

def p_code(p):
    'code : YEAR'
    # print "Code rule"
    p[0] = p[1]

def p_code_number(p):
    'code : NUMBER'
    # print "Code number rule"
    p[0] = p[1]

def p_publication(p):
    'publication : IEEE text MONTH YEAR'
    # print "Publication rule"
    p[0] = p[2] + p[3] + str(p[4])

def p_abstract(p):
    'abstract : ABSTRACT text INDEX'
    # print "Abstract rule"
    p[0] = p[2]

def p_keywords(p):
    'keywords : text TERMS text'
    # print "Keywords rule"
    p[0] = p[1] + p[3]

def p_content(p):
    'content : chapter_seq REFERENCES'
    # print "Content rule"
    p[0] = Content(p[1])
    # p[0].show()

def p_chapter_seq_r(p):
    'chapter_seq : chapter chapter_seq'
    # print "Chapter Sequence recursive rule"
    p[0] = [p[1], p[2]]

def p_chapter_seq(p):
    'chapter_seq : chapter'
    # print "Chapter Sequence rule"
    p[0] = p[1]

def p_chapter(p):
    'chapter : CHAPTER_MARK ctext'
    # print "Chapter rule"
    p[0] = Chapter(p[1], p[2])
    # p[0].show()

def p_ctext_year(p):
    'ctext : YEAR ctext'
    # print "Chapter text year rule"
    p[0] = str(p[1]) + p[2]

def p_ctext_number(p):
    'ctext : NUMBER ctext'
    # print "Chapter text number rule"
    p[0] = str(p[1]) + p[2]

def p_ctext_text(p):
    'ctext : GENERAL ctext'
    # print "Chapter text text rule"
    p[0] = p[1] + p[2]

def p_ctext_ieee(p):
    'ctext : IEEE ctext'
    # print "Chapter text IEEE rule"
    p[0] = p[1] + p[2]

def p_ctext(p):
    'ctext : '
    # print "Chapter text rule"
    p[0] = ''

def p_references(p):
    'references : reference_seq ctext'
    # print "References rule"
    p[0] = p[1]
    
def p_reference_seq_B(p):
    'reference_seq : REFERENCE_B reference_seq'
    # print "References B rule"
    p[0] = [p[1], p[2]]

# def p_reference_seq_L(p):
#     'reference_seq : REFERENCE_L reference_seq'
    # print "References Link rule"
#     p[0] = [p[1], p[2]]

def p_reference_seq_general(p):
    'reference_seq : text reference_seq'
    # print "Reference seq general rule"
    p[0] = [p[1], p[2]]

def p_reference_seq(p):
    'reference_seq : '
    # print "Reference seq none rule"
    p[0] = None

def p_titleandauthor(p):
    'titleandauthor : text'
    # print "Title and author rule"
    p[0] = p[1]

def p_text_general(p):
    'text : GENERAL text'
    # print "Text general rule"
    p[0] = p[1] + p[2]

def p_text_number(p):
    'text : code text'
    # print "code general rule"
    p[0] = str(p[1]) + p[2]

def p_text(p):
    'text : GENERAL'
    # print "Text rule"
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)

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
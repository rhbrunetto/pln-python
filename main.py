# +-------------------------------------------+
# |     Ricardo Henrique Brunetto - 94182     |
# |            Thiago Kira - 78750            |
# |                                           |
# |     PROCESSAMENTO DE LINGUAGEM NATURAL    |
# |                 EM PYTHON                 |
# |                                           |
# |    Inteligencia Artificial I - DIN/UEM    |
# |                                           |
# |                 Jun/2018                  |
# +-------------------------------------------+
from __future__ import print_function
import os
import re
import fileinput
import plymodule
import operator
from nltk.corpus import stopwords
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from cStringIO import StringIO

def_stop_words = ['.', '...', ',', 'the' ]
stop_words = list(stopwords.words('english'))
stop_words.extend(def_stop_words)
stop_words = [x.encode('utf-8') for x in stop_words]

def pdf_to_text(pdfname):
    """Converts a PDF file to text"""
    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Extract text
    fp = file(pdfname, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()

    # Get text from StringIO
    text = sio.getvalue()

    # Cleanup
    device.close()
    sio.close()

    return text

def process(path):
    text_file = open(path+".txt", "w")
    text_file.write(pdf_to_text(path))
    text_file.close()
    return

def cont_words(file):
    word_cont = {}
    with open(file) as f:
        for line in f:
            for word in line.replace(',' or '.' or '(' or ')' , ' ').split():
                word_lower = word.lower()
                if word_lower in word_cont.keys():
                    word_cont[word_lower] += 1
                else:
                    if ((word_lower not in stop_words) and (not word_lower.isdigit()) and (len(word_lower) > 2) and (not word_lower.endswith('.'))):
                        word_cont[word_lower] = 1
    sorted_by_value = sorted(word_cont.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_by_value 

def split_header(file):
    f = fileinput.FileInput(file, inplace=True )
    found = False
    for lines in f:
        if ('APRIL' in lines) and (not found):
            print(lines.replace('APRIL', '\nAPRIL'), end="")
            found = True
        elif ('JANUARY' in lines) and (not found):
            print(lines.replace('JANUARY', '\nJANUARY'), end='')
            found = True
        elif ('FEBRUARY' in lines) and (not found):
            print(lines.replace('FEBRUARY', '\nFEBRUARY'), end='')
            found = True
        elif ('MARCH' in lines) and (not found):
            print(lines.replace('MARCH', '\nMARCH'), end='')
            found = True
        elif ('MAY' in lines) and (not found):
            print(lines.replace('MAY', '\nMAY'), end='')
            found = True
        elif ('JUNE') in lines and (not found):
            print(lines.replace('JUNE', '\nJUNE'), end='')
            found = True
        elif ('JULY' in lines) and (not found):
            print(lines.replace('JULY', '\nJULY'), end='')
            found = True
        elif ('AUGUST') in lines and (not found):
            print(lines.replace('AUGUST', '\nAUGUST'), end='')
            found = True
        elif ('SEPTEMBER') in lines and (not found):
            print(lines.replace('SEPTEMBER', '\nSEPTEMBER'), end='')
            found = True
        elif ('OCTOBER') in lines and (not found):
            print(lines.replace('OCTOBER', '\nOCTOBER'), end='')
            found = True
        elif ('NOVEMBER') in lines and (not found):
            print(lines.replace('NOVEMBER', '\nNOVEMBER'), end='')
            found = True
        elif ('DECEMBER' in lines) and (not found):
            print(lines.replace('DECEMBER', '\nDECEMBER'), end='')
            found = True
        else:
            print(lines, end='')

def convert_to_text(directory):
    os.system("ls " + directory + "*.pdf > .tmpfiles")
    with open(".tmpfiles", "r") as ins:
       files = ins.readlines()
       for arq in files:
           print("Converting " + arq)
           process(arq.replace('\n', ''))
    os.system("rm .tmpfiles")

def apply_preprocess(directory):
    os.system("ls " + directory + "*.pdf.txt > .tmpfiles")
    with open(".tmpfiles", "r") as ins:
       files = ins.readlines()
       for arq in files:
           print("Pre-processing " + arq)
           split_header(arq.replace('\n', ''))
    os.system("rm .tmpfiles")

def apply_pln(path):
    print("Parsing " + path)
    article = plymodule.parsing(path)
    article.setTopTen(cont_words(path)[0:10])
    output = path.replace('.pdf.txt', '.out')
    with open(output, "w") as out:
        out.write(article.toString())
    out.close()

def parse(directory):
    os.system("ls " + directory + "*.pdf.txt > .tmpfiles")
    with open(".tmpfiles", "r") as ins:
       files = ins.readlines()
       for arq in files:
           apply_pln(arq.replace('\n', ''))
    os.system("rm .tmpfiles")

def main():        
    directory = "files/"
    convert_to_text(directory)
    apply_preprocess(directory)
    parse(directory)
    
if __name__ == "__main__":
    main()

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
# import plymodule
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
    # print(path)
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
    for lines in f:

        if 'APRIL' in lines:
            print(lines.replace('APRIL', '\nAPRIL'), end="")

        elif 'JANUARY' in lines:
            print(lines.replace('JANUARY', '\nJANUARY'), end='')

        elif 'FEBRUARY' in lines:
            print(lines.replace('FEBRUARY', '\nFEBRUARY'), end='')

        elif 'MARCH' in lines:
            print(lines.replace('MARCH', '\nMARCH'), end='')
                
        elif 'MAY' in lines:
            print(lines.replace('MAY', '\nMAY'), end='')

        elif 'JUNE' in lines:
            print(lines.replace('JUNE', '\nJUNE'), end='')

        elif 'JULY' in lines:
            print(lines.replace('JULY', '\nJULY'), end='')
               
        elif 'AUGUST' in lines:
            print(lines.replace('AUGUST', '\nAUGUST'), end='')

        elif 'SEPTEMBER' in lines:
            print(lines.replace('SEPTEMBER', '\nSEPTEMBER'), end='')
                
        elif 'OCTOBER' in lines:
            print(lines.replace('OCTOBER', '\nOCTOBER'), end='')

        elif 'NOVEMBER' in lines:
            print(lines.replace('NOVEMBER', '\nNOVEMBER'), end='')

        elif 'DECEMBER' in lines:
            print(lines.replace('DECEMBER', '\nDECEMBER'), end='')
                
        else:
            print(lines, end='')

def main():
            
    directory = "files/"
    os.system("ls " + directory + "*.pdf > .tmpfiles")
    with open(".tmpfiles", "r") as ins:
       files = ins.readlines()
       for arq in files:
           process(arq.replace('\n', ''))
        #    split_header(arq.replace('.pdf', '.pdf.txt'))
    os.system("rm .tmpfiles")
    # os.system("ls " + directory + "*.pdf.txt > .tmpfiles")
    # with open(".tmpfiles", "r") as ins:
    #    files = ins.readlines()
    #    for arq in files:
    #        split_header(arq.replace('\n', ''))
    #     #    split_header(arq.replace('.pdf', '.pdf.txt'))
    # os.system("rm .tmpfiles")
    #print(pdf_to_text("/home/ricardo/Downloads/analise-de-desempenho.pdf"))
    # d = cont_words('files/118.pdf.txt') 
    # split_header('files/118.pdf.txt')
    
if __name__ == "__main__":
    main()

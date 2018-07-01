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
stop_words = [x.encode('ascii') for x in stop_words]

def pdf_to_text(pdfname):
    """Converts a PDF file to text"""
    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    codec = 'ascii'
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
            for word in line.replace(',' or '.', ' ').split():
                word_lower = word.lower()
                if word_lower in word_cont.keys():
                    word_cont[word_lower] += 1
                else:
                    if ((word_lower not in stop_words) and (not word_lower.isdigit()) and (len(word_lower) > 1)):
                        word_cont[word_lower] = 1
    sorted_by_value = sorted(word_cont.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_by_value 

def split_header(file):
    f = fileinput.FileInput(file, inplace=True )
    for lines in f:

        if 'APRIL' in lines:
            print(lines.replace('APRIL', '\nAPRIL'))

        elif 'JANUARY' in lines:
            print(lines.replace('JANUARY', '\nJANUARY'))

        elif 'FEBRUARY' in lines:
            print(lines.replace('FEBRUARY', '\nFEBRUARY'))

        elif 'MARCH' in lines:
            print(lines.replace('MARCH', '\nMARCH'))
                
        elif 'MAY' in lines:
            print(lines.replace('MAY', '\nMAY'))

        elif 'JUNE' in lines:
            print(lines.replace('JUNE', '\nJUNE'))

        elif 'JULY' in lines:
            print(lines.replace('JULY', '\nJULY'))
               
        elif 'AUGUST' in lines:
            print(lines.replace('AUGUST', '\nAUGUST'))

        elif 'SEPTEMBER' in lines:
            print(lines.replace('SEPTEMBER', '\nSEPTEMBER'))
                
        elif 'OCTOBER' in lines:
            print(lines.replace('OCTOBER', '\nOCTOBER'))

        elif 'NOVEMBER' in lines:
            print(lines.replace('NOVEMBER', '\nNOVEMBER'))

        elif 'DECEMBER' in lines:
            print(lines.replace('DECEMBER', '\nDECEMBER'))
                
        else:
            print(lines)

def main():
            
    directory = "allfiles/"
    #os.system("ls " + directory + "*.pdf > .tmpfiles")
    #with open(".tmpfiles", "r") as ins:
    #    files = ins.readlines()
    #    for arq in files:
    #        process(arq.replace('\n', ''))
    #os.system("rm .tmpfiles")
    #print(pdf_to_text("/home/ricardo/Downloads/analise-de-desempenho.pdf"))
    #d = cont_words('allfiles/118.pdf.txt') 
    #print d
    #print len(d)
    
if __name__ == "__main__":
    main()

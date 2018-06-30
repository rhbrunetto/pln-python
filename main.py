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
import plymodule.lexer
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from cStringIO import StringIO

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

def main():
    directory = "/home/ricardo/uem/ia/t2/files/"
    os.system("ls " + directory + "*.pdf > .tmpfiles")
    with open(".tmpfiles", "r") as ins:
        files = ins.readlines()
        for arq in files:
            process(arq.replace('\n', ''))
    os.system("rm .tmpfiles")
    # print(pdf_to_text("/home/ricardo/Downloads/analise-de-desempenho.pdf"))
            


if __name__ == "__main__":
    main()
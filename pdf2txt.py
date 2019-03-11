#!c:\users\shule\appdata\local\programs\python\python37-32\python.exe

"""
Converts PDF text content (though not images containing text) to plain text, html, xml or "tags".
"""
import argparse
import logging
import six
import sys
import pdfminer.settings
pdfminer.settings.STRICT = False
import pdfminer.high_level
'''def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)

        # get the first page
        page = pdf.getPage(1)
        print(page)
        #print('Page type: {}'.format(str(type(page))))

        text = page.extractText()
        print(text)
'''
import os
from os import chdir, getcwd, listdir, path
import codecs
from PyPDF2 import PdfFileReader
from time import strftime

def check_path(prompt):
    ''' (str) -> str
    Verifies if the provided absolute path does exist.
    '''
    abs_path = input(prompt)
    while path.exists(abs_path) != True:
        print ("The specified path does not exist.")
        abs_path = input(prompt)
    return abs_path

print ()

folder = check_path("Provide absolute path for the folder: ")

list=[]
directory=folder
for root,dirs,files in os.walk(directory):
    for filename in files:
        if filename.endswith('.pdf'):
            t=os.path.join(directory,filename)
            list.append(t)
print (list)
path=list[0]
head,tail=os.path.split(path)
var="\\"

tail=tail.replace(".pdf",".txt")
name=head+var+tail



content = ""
# Load PDF into pyPDF
pdf = PdfFileReader(open(path, "rb"))
# Iterate pages
for j in range(0, pdf.getNumPages()):
    # Extract text from page and add to content
    pageObj=pdf.getPage(j).extractText()
    content += str(pageObj.encode('ascii', 'ignore'))
    content.replace('/n', "")
f=open("f",'w')
print (content.encode('UTF-8'))
f.write(str(content.encode('ascii', 'ignore')))
f.close
\
import pdfminer.layout
from pdfminer.image import ImageWriter
from cStringIO import StringIO
from pdfminer.converter import LTChar, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

def pdf_to_csv(filename):
    class CsvConverter(TextConverter):
        def __init__(self, *args, **kwargs):
            TextConverter.__init__(self, *args, **kwargs)

        def end_page(self, i):
            from collections import defaultdict
            lines = defaultdict(lambda : {})
            for child in self.cur_item._objs:                #<-- changed
                if isinstance(child, LTChar):
                    (_,_,x,y) = child.bbox
                    line = lines[int(-y)]
                    line[x] = child._text.encode(self.codec) #<-- changed

            for y in sorted(lines.keys()):
                line = lines[y]
                self.outfp.write(";".join(line[x] for x in sorted(line.keys())))
                self.outfp.write("\n")

    # ... the following part of the code is a remix of the
    # convert() function in the pdfminer/tools/pdf2text module
    rsrc = PDFResourceManager()
    outfp = StringIO()
    device = CsvConverter(rsrc, outfp, codec="utf-8", laparams=LAParams())
        # becuase my test documents are utf-8 (note: utf-8 is the default codec)

    doc = PDFDocument()
    fp = open(filename, 'rb')
    parser = PDFParser(fp)
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')

    interpreter = PDFPageInterpreter(rsrc, device)

    for i, page in enumerate(doc.get_pages()):
        outfp.write("START PAGE %d\n" % i)
        if page is not None:
            interpreter.process_page(page)
        outfp.write("END PAGE %d\n" % i)

    device.close()
    fp.close()

    return outfp.getvalue()
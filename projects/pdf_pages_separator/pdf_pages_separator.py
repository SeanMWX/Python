# import package
from PyPDF2 import PdfFileReader, PdfFileWriter
import re

# load config file
f = open("config.txt", "r")
lines = f.read()

# check document name & pages number
pattern = re.compile(r'\[[^\[]*\]')
results = pattern.findall(lines)
# check document name
pdf_document = results[0][1:-1]
# check pages number
pages_list = results[1][1:-1].split(',')
pages = []
for page in pages_list:
    if '-' in page:
        page = page.split('-')
        start = int(page[0])
        end = int(page[1])
        for i in range(start,end+1):
            pages.append(i)
    else:
        pages.append(int(page))

# seperate the pdf by pages number
pdf = PdfFileReader(pdf_document)
for page in pages:
    pdf_write = PdfFileWriter()
    current_page = pdf.getPage(page)
    pdf_write.addPage(current_page)

    outputFilename = 'pdf/%d.pdf' % (page)
    with open(outputFilename, 'wb') as out:
        pdf_write.write(out)

# output the results
print('Successfully separated all pages: [%s]' % (' '.join([str(elem) for elem in pages])))
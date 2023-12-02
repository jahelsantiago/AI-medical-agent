#read a pdf 
import PyPDF2


def read_pdf():
    # read pdf file
    pdfFileObj = open('sample.pdf', 'rb')
    # create pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # print number of pages in pdf file
    print(pdfReader.numPages)
    # create a page object
    pageObj = pdfReader.getPage(0)
    # extract text from page
    print(pageObj.extractText())
    # close the pdf file
    pdfFileObj.close()

read_pdf()
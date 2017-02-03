import pyPdf
import sys

if __name__ == "__main__":
    input1 = pyPdf.PdfFileReader(file("01011B00-200ppp-20hojas.PDF", "rb"))
    output = pyPdf.PdfFileWriter()
    num_page = 1
    page_for_doc = 1
    for p1 in input1.pages:
        output.addPage(p1)
        if num_page % page_for_doc == 0:
            outputStream = file(("page_" + str(num_page) + ".pdf"), "wb")
            output.write(outputStream)
            output = pyPdf.PdfFileWriter()
            outputStream.close()
        else:
            if num_page == input1.getNumPages():
                outputStream = file(("page_" + str(num_page) + ".pdf"), "wb")
                output.write(outputStream)
                outputStream.close()
        num_page = num_page + 1"""




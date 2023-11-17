from pdf2docx import Converter

pdf_path = "sample.pdf" #  need to change as the name of document.
docx_path = "output.docx"

cv = Converter(pdf_path)
cv.convert(docx_path)
cv.close()


from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
pdf = PdfFileReader(open('pdfSource.pdf', 'rb'))
output.addPage(pdf.getPage(0))
outputStream = open('pdfGenerated.pdf', 'wb')
output.write(outputStream)
#! python3
# Crypt all pdf in the current working directory

import os, PyPDF2

def cryptItAll(folder):
	absPath = os.path.abspath(folder)
	
	# find all pdf
	for folder, subfolders, files in os.walk(absPath):
		for file in files:
			if file.endswith('.pdf'):
				pdfFile = open(file, 'rb')
				pdfReader = PyPDF2.PdfFileReader(pdfFile)
				pdfWriter = PyPDF2.PdfFileWriter()
				for pageNum in range(pdfReader.numPages):
					pdfWriter.addPage(pdfReader.getPage(pageNum))
				pdfWriter.encrypt('sunburn')
				encryptedFile = open('encrypted_' + file, 'wb')
				pdfWriter.write(encryptedFile)
				encryptedFile.close()

cryptItAll('.')

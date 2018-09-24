#! /usr/bin/python3
# Create automatic multiplication table

import openpyxl, sys

def multiplyIt(num):
	wb = openpyxl.Workbook()
	ws = wb.active
	ws.title = "Multiplication table"

	for r in range(1, num):
		for c in range(1, num):
			ws.cell(row=r, column=c).value = r * c

	wb.save("multip.xlsx")


num = int(sys.argv[1]) + 1
multiplyIt(num)

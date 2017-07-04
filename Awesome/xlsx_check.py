import xlsxwriter
workbook = xlsxwriter.Workbook("DuckDuckGo.xlsx")
worksheet = workbook.add_worksheet()
row = 0
col = 0
A = ["Arik Pamnani", "He is a student of IIT Gandhinagar", 8.50]
B = ["Shivdutt Sharma", "He is also a student of IIT Gandhinagar", 7.67]
for name, designation, cpi in [A, B]:
	worksheet.write(row, col, name)
	worksheet.write(row, col+1, designation)
	worksheet.write(row, col+2, cpi)
	row += 1
workbook.close()


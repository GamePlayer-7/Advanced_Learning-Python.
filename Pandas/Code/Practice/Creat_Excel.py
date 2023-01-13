from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

sheet['A1'] = "I am"
sheet['B1'] = "Python"
sheet['C1'] = "Developer."

wb.save("creat_excel.xlsx")

from openpyxl import Workbook

wb = Workbook()
sheet = wb.active

sheet['A1'] = "I am "
sheet['B1'] = "learning"
sheet['C1'] = "Python"

wb.save("Learning.xlsx")

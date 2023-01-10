from openpyxl import load_workbook

wb = load_workbook('wb1.xlsx')

sheet = wb.active

print(sheet["A1"].value)
print(sheet["B1"].value)
print(sheet["C1"].value)
print(sheet["D1"].value)

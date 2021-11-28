import openpyxl as xl

wb = xl.load_workbook('data.xlsx')
sheet = wb['Sheet1']
cell = sheet['a1'] # a = column and 1 = row
cell = sheet.cell(1,1) # 1 = row , 1 = column

print(cell.value)


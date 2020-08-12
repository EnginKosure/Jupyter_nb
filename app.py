import openpyxl as xl
from openpyxl.chart import BarChart, Reference
wb = xl.load_workbook('transactions.xlsx')
# print(wb['Sheet1'])
sheet = wb['Sheet1']
# print(sheet)
cell = sheet['A1']
# cell = sheet.cell(1, 1)
print(cell)
print(sheet.max_row)

for row in range(2, sheet.max_row+1):
    cell = sheet.cell(row, 3)
    corrected_price = cell.value*0.9
    print(corrected_price)
    corrected_new_val = sheet.cell(row, 4)
    corrected_new_val.value = corrected_price

values = Reference(sheet, min_row=2, max_row=sheet.max_row,
                   min_col=4, max_col=4)
chart = BarChart()
chart.add_data(values)
sheet.add_chart(chart, 'e2')
wb.save('transactions2.xlsx')

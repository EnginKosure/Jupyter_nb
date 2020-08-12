import openpyxl as xl
wb = xl.load_workbook('transactions.xlsx')
# print(wb['Sheet1'])
sheet = wb['Sheet1']
# print(sheet)

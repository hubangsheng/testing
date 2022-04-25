import time

import openpyxl

# 获取工作表
book = openpyxl.load_workbook("openpyxlDemo.xlsx")

# 读取工作表
sheet = book.active

# 读取单个单元格
cell_a1 = sheet['A1']
cell_a3 = sheet.cell(column=1, row=3)

# 读取多个连续单元格
cells = sheet["A1":"A3"]


# 获取单元格的值
print(cell_a1.value)
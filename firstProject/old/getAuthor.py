import re

import xlrd
import xlwt

# 读取Excel文件内容
input = input("Inpurt you file:")
data = xlrd.open_workbook(input)
# data = xlrd.open_workbook("C:/Users/Administrator/Desktop/中国作者.xlsx")
table = data.sheets()[0]
nrows = table.nrows

# 新建输出的Excel文件
wb = xlwt.Workbook()
ws = wb.add_sheet('Chinese author')

# 初始化写入文件行坐标
row = 0
print("Output Chinese author:")
for i in range(nrows):
    if 1 <= i:
        col_B_value = table.cell(i, 1).value
        strList = re.split(r'(\[(\w\b)*)', col_B_value)
        for val in strList:
            if val and (";" in val) and("]" in val) and (("China" in val) or "Taiwan" in val):
                ws.write(row, 0, val[0:val.rfind(']', 1)])
                row += 1
wb.save('Output.xlsx')
print("Output.xlsx写入成功！")

data = xlrd.open_workbook('Output.xlsx')
table = data.sheets()[0]
nrows = table.nrows
wb = xlwt.Workbook()
ws2 = wb.add_sheet('author')

authorList = []
row = 0
for i in range(nrows):
    col_B_value = table.cell(i, 0).value
    strList = re.split(r';', col_B_value)
    for str in strList:
        if str not in authorList:
            authorList.append(str)
            ws2.write(row, 0, str)
            row += 1

print("我国学者为%s人" % authorList.__len__())
wb.save('Output1.xlsx')
print("Output1.xlsx写入成功！")



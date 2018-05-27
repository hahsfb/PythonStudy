import re

import xlrd
import pandas as pd

# 读取Excel文件内容
# input = input("Inpurt you file:")
# data = xlrd.open_workbook(input)
data = xlrd.open_workbook("D:/Document/WeChat Files/hsfbhao539/Files/统计作者数.xlsx")
table = data.sheets()[0]
nrows = table.nrows

# 新建输出的Excel文件
# wb = xlwt.Workbook()
# ws = wb.add_sheet('Author Count')

# 初始化写入文件行坐标
row = 0
print("CSV文件写入中...")
allList = []
for i in range(nrows):
    if 1 <= i:
        col_B_value = str(table.cell(i, 0).value)
        col_B_value = col_B_value.replace('[', '')
        col_B_value = col_B_value.replace('"', '')
        col_B_value = col_B_value.replace(']', '')
        col_B_value = col_B_value.replace("'", '')
        col_B_value = col_B_value.lstrip()
        strList = re.split(';', col_B_value)
        for name in strList:
            allList.append(name)

AuthorList = set(allList)

df = []
for name in AuthorList:
    cnt = allList.count(name)
    a = [name, cnt]
    df.append(a)

df = pd.DataFrame(df, columns=['name', 'count'])

df.to_csv('AuthorCount.csv', index=False)
print("AuthorCount.csv写入成功！")

import itertools

import xlrd
import pandas as pd

# 读取Excel文件内容
# input = input("Inpurt you file:")
# data = xlrd.open_workbook(input)
data = xlrd.open_workbook("D:/Document/WeChat Files/hsfbhao539/Files/1.5作者.xlsx")
table = data.sheets()[0]
nrows = table.nrows

# 初始化写入文件行坐标
row = 0
print("CSV文件写入中...")

record = []
for i in range(nrows):
    if 1 <= i:
        a = str(table.cell(i, 0).value)
        # a = str(name.values.tolist())
        a = a.replace('[', '')
        a = a.replace(']', '')
        a = a.replace("'", '')
        a = a.replace(" ", '')
        a = a.replace('"', '')
        a = a.split(';')
        c = list(itertools.combinations(a, 2))
        if len(c) > 1:
            for b in c:
                record.append(b)
# z = record
print(len(record))
record = list(set(record))
print(len(record))

record = pd.DataFrame(record, columns=['source', 'target'])
# record['type'] = 'undirected'
record.to_csv('AuthorRelation.csv', index=False)
print("AuthorRelation2.csv写入成功！")


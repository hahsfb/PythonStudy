import itertools

import csv
import xlrd
import pandas as pd

# 读取csv文件作者关系数据
relations = []
csv_reader = csv.reader(open('D:/Document/WeChat Files/hsfbhao539/Files/AuthorRelation.csv', encoding='utf-8'))
# for row in csv_reader:
#     relations.append(row)


# 读取Excel文件内作者的姓名
data = xlrd.open_workbook("D:/Document/WeChat Files/hsfbhao539/Files/20个施引作者.xlsx")
table = data.sheets()[0]
nrows = table.nrows

print("CSV文件写入中...")
record = []

for row in csv_reader:
    for i in range(nrows):
        name = str(table.cell(i, 0).value).replace(' ', '')
        if name in row:
            record.append(row)


# for i in range(nrows):
#     name = str(table.cell(i, 0).value).replace(' ', '')
#     print(name)
#     for row in relations:
#         if name in row:
#             record.append(row)
# z = record
print(len(record))
# record = list(set(record))
# print(len(record))

record = pd.DataFrame(record, columns=['source', 'target'])
# record['type'] = 'undirected'
record.to_csv('AuthorRelation2.csv', index=False)
print("AuthorRelation2.csv写入成功！")


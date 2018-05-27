import re
import itertools
import xlrd
import xlwt
import pandas as pd

# 读取Excel文件内容
# input = input("Inpurt you file:")
# data = xlrd.open_workbook(input)
data = xlrd.open_workbook("D:/Document/WeChat Files/hsfbhao539/Files/原文机构.xlsx")
table = data.sheets()[0]
nrows = table.nrows

# 新建输出的Excel文件
wb = xlwt.Workbook()
ws = wb.add_sheet('First author')

# 初始化写入文件行坐标
relation = []
authorList = []
print("Output First author:")
for i in range(nrows):
    row_list = []
    if 1 <= i:
        col_B_value = str(table.cell(i, 0).value)
        strList = re.split(r'(\[(\w\b)*)', col_B_value)
        for val in strList:
            if val and "]" in val:
                row_list.append(val[val.rfind(']', 1)+1:].split(',')[0].lstrip())

    row_list = list(set(row_list))
    if row_list and len(row_list) > 0:
        authorList.extend(row_list)

    row_list = list(itertools.combinations(row_list, 2))
    if len(row_list) > 0:
        for b in row_list:
            relation.append(b)


relation = pd.DataFrame(relation, columns=['source', 'target'])
# record['type'] = 'undirected'
relation.to_csv('FirstAuthorRelation.csv', index=False)
print("FirstAuthorRelation.csv写入成功！")

df = []
for name in list(set(authorList)):
    cnt = authorList.count(name)
    a = [name, cnt]
    df.append(a)

df = pd.DataFrame(df, columns=['name', 'count'])

df.to_csv('FirstAuthorCount.csv', index=False)
print("FirstAuthorCount.csv写入成功！")

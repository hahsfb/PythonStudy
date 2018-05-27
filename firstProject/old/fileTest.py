#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd
import json
from xlutils.copy import copy

# file = open('aa.txt', 'w+')
# print(file.name)
# print(file.mode)
# for file_line in file:
#     print(file_line, end='')

# file.write('www.runoob.com!\nVery good site!\n')
# file.close()
jsonData = []
test = [('aa', 1, '男', '2017'), ('bb', 2, '男', '2017'), ('cc', 3, '男', '2017'), ('dd', 4, '男', '2017')]
for row in test:
    result = {}
    result['name'] = row[0]
    result['age'] = row[1]
    result['sex'] = row[2]
    result['time'] = row[3]
    jsonData.append(result)

print('原始数据jsonData================')
print(jsonData)
# after = json.dumps(jsonData, ensure_ascii=False)
# after = jsondatar[1:len(jsondatar) - 1]
print('转换为json格式的数据after================')
print(jsonData)
for aa in jsonData:
    # print(aa)
    print(aa['name'], end=' ')
    print(aa['age'])
    # print(aa.name)
    # print(aa.age)
    # print(aa.sex)
    # print(aa.time)
    # print('========================')

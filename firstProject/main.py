import boto3
import xlrd, xlwt
import re

# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)


# str = re.split(r'(\[(\w\b)*)', str1)
# str3 = re.split(r'(\[\w\]?)', str1)

data = xlrd.open_workbook('Output.xlsx')
table = data.sheets()[0]
nrows = table.nrows

authorList = []
for i in range(nrows):
    col_B_value = table.cell(i, 0).value
    strList = re.split(r';', col_B_value)
    for str in strList:
        if str not in authorList:
            authorList.append(str)
print(authorList)
print(authorList.__len__())

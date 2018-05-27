#! /usr/bin/evn python3
# -*- coding: utf-8 -*-

import string

print(string.ascii_letters)

a_list = range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

b_list = [x * x for x in a_list]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

c_dict = {x: string.ascii_letters[x] for x in a_list}
# {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j'}

# 写一个程序，打印数字1到100，3的倍数打印“Fizz”来替换这个数，5的倍数打印“Buzz”，对于既是3的倍数又是5的倍数的数字打印“FizzBuzz”。
# for i in range(1, 101): print('Fizz'[i % 3 * 4::] + "Buzz"[i % 5 * 4::] or i)


iterable = 'asdfghjk'
i = 0
for item in iterable:
    print(i, " ", item)
    i += 1

for i, item in enumerate(iterable):
    print(i, " ", item)

print(list(enumerate('abc')))
# [(0, 'a'), (1, 'b'), (2, 'c')]

print(list(enumerate('abc', 1)))
# [(1, 'a'), (2, 'b'), (3, 'c')]


# 字典/集合 生成
my_dict = {i: i * i for i in range(10)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
my_set = {i * 15 for i in range(10)}
# {0, 135, 105, 75, 45, 15, 120, 90, 60, 30}

for key, value in my_dict.items():
    print(key, value)

testTuple = (1, 2, 3, 4)
for x in testTuple[::-1]:
    print(x)

temStr = "Hello Java, Hello Python, Use JavaScript"
print(temStr.replace("Hello", "Bye"))

import re

rex = r'(Hello|Use)'
print(re.sub(rex, "Bye", temStr))
print(re.subn(rex, "Bye", temStr))

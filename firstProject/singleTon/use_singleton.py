#from singleTon.mysingleton import my_singleton

#my_singleton.foo()


from functools import reduce


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(lambda x, y: x + y, map(char2num, '13579'), 100))

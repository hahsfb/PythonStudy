from functools import reduce

#
#
# def format_name(s):
#     return s.title()
#
# print(format_name("aasasfds"))
# print(list(map(format_name, ['adam', 'LISA', 'barT'])))
#
# def prod(x, y):
#     return x*y
#
# print(reduce(prod, [2, 4, 5, 7, 12]))
#
# import math
#
# def is_sqr(x):
#     r = int(math.sqrt(x))
#     return r*r==x
#
# print(list(filter(is_sqr, range(1, 10))))


a = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(a, key=str.lower))


# def calc_prod(lst):
#     def a():
#         def lazy_prod(l1, l2):
#             return l1*l2
#         return reduce(lazy_prod, lst)
#     return a
#
# f = calc_prod([1, 2, 3, 4])
# print(f())

def count():
    fs = []
    for i in range(1, 4):
        def f(bb):
            return lambda: bb * bb

        fs.append(f(i))
    return fs


f1, f2, f3 = count()

print(f1(), f2(), f3())

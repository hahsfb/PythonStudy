from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['jen'] = 'python'
favorite_language['sarach'] = 'c'
favorite_language['edward'] = 'ruby'
favorite_language['phil'] = 'python'

print(type(favorite_language))

for name, value in favorite_language.items():
    print(name, value)

print("favorite_language.get('jen'): %s" % favorite_language.get('jen'))
print("favorite_language.values(): %s" % favorite_language.values())
# favorite_language.fromkeys(['jen'], value='haha')
# print(favorite_language)

print("favorite_language.clear(): %s" % favorite_language.pop('jen'))
print("favorite_language.clear(): %s" % favorite_language.clear())


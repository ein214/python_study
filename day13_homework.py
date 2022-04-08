sentence = ('hello', 'this is python', 'ok, bye~')
dict = {}

for item in sentence:
    dict[item] = len(item)

print(dict)
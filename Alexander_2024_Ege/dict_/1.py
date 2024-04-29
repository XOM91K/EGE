sl = {1: 5, 11: 22, 'hello': 99}
print(sl['hello'])
print(list(sl.values()))
print(list(sl.keys()))
print(list(sl.items()))
print(sl.get('hello1', 'ключа нет'))
h = [('g', 5), (77, 100)]
print(sl.fromkeys(h, 5))
print(sl)
sl.setdefault(12, 100)
print(sl)
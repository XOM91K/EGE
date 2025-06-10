import itertools
ct = 0
# set - множества
#убирает дублирования
for x in set(itertools.permutations('СПОРТЛОТО')):
    x = ''.join(x)
    if 'ТТ' in x:
        ct += 1
print(ct)
# int, str, float, bool
# tuple (кортеж)
# set (множества)
# list (списки)
# dict (словарь)
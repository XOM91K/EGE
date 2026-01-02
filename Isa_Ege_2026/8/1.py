import itertools
k = 0
for x in itertools.product(sorted('ЖЧГМЯФИ'), repeat=6):
    x = ''.join(x)
    k += 1
    #if x[0] == 'Ж' and x[1] == 'Я':
    if x[:2] == 'ЖЯ':
        print(k, x)
# for x in itertools.product('СН', repeat=2):
#     print(x)
# t = itertools.product('СН', repeat=2)
# print(list(t))
# s = itertools.permutations('СНЕГ', 3)
# print(list(s))

# for x in [0, 1, 2, 3, 4]:
#     print(x)
# print(list(range(5)))

# l = ['С', 'Н', 'Е', 'Г']
# l = 'СНЕГ'
# if 'ЕГ' in l:
#     print('да есть')
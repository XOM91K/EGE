import itertools
k = 0
for x in itertools.product(sorted('АРГУМЕНТ'), repeat=4):
    x = ''.join(x)
    k = k + 1
    if len(set(x)) == len(x):
        if sorted(x) == list(x):
            print(k, x)
    #if x[:4] == 'АЕМУ':


# ab = 'аппарат'
# if len(set(ab)) == len(ab):
#     print('Да')
# else:
#     print('Нет')
# s = 'АГДБВ'
# print(sorted(s) == list(s))
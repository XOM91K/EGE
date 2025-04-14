# Комбинаторика

#Перестановки
import itertools  #iteration tools
# ct = 0
# for x in itertools.permutations('ёлка', r=4):
#     x = ''.join(x)
#     ct += 1
# print(ct)

#ёлка
# # 4! = 1 * 2 * 3 * 4 = 24
# ct = 0
# for s1  in 'ёлка':
#     for s2 in 'ёлка':
#         for s3 in 'ёлка':
#             for s4 in 'ёлка':
#                 slovo = s1 + s2 + s3 + s4
#                 if len(set(slovo)) == 4:
#                     #if
#                     print(slovo)
#                     ct += 1
# print(ct)


#Комбинации
ct = 0
for x in itertools.product('СТОЛ'):
    x = ''.join(x)
    print(x)
    ct += 1
print(ct)
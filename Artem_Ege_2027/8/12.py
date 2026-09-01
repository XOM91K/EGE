# import itertools
# l = []
# for x in itertools.permutations('АМФИБРАХИЙ'):
#     x = ''.join(x)
#     if x[4] == 'Б' and x[5] == 'Р':
#         l.append(x)
# print(len(set(l)))
# import itertools
# ct = 0
# for x in set(itertools.permutations('АМФИБРАХИЙ')):
#     x = ''.join(x)
#     if x[4] == 'Б' and x[5] == 'Р':
#         ct += 1
# print(ct)
import itertools
ct = 0
for x in set(itertools.permutations('АМФИБРАХИЙ')):
    x = ''.join(x)
    if 'ААФИИ' in x or 'ИИФАА' in x:
            ct += 1
print(ct)
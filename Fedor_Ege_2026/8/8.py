import itertools
ct = 0
for x in set(itertools.permutations('АМФИБРАХИЙ')):
    x = ''.join(x)
    if 'ААФИИ' in x or 'ИИФАА' in x:
        print(x)
        ct += 1
print(ct)
# s = 'abracadabra'
# print(set(s))
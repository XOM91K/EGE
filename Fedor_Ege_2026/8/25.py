import itertools
l = list(itertools.product(sorted('АИКЛМЬ'), repeat=6))
l2 = []
for x in l:
    x = ''.join(x)
    l2.append(x)
    # if x[0] == 'К' and x[-1] == 'Ь'
# print(l2)
# x = 'ИИММКА'
# print(l2.index(x[::-1]), l2[3607], l2.index(x))
for x in l2:
    if x[0] == 'К' and x[-1] == 'Ь' and len(set(x)) == 6:
        pos_per = l2.index(x[::-1])
        pos_tek = l2.index(x)
        if abs(pos_per - pos_tek) == 26655:
            print(x, sum(map(int, str(pos_tek + 1))))
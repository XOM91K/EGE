import math
l = [[int(d) for d in x.split()] for x in open('13.txt')]
S = 6089572
mn_sm = 10 ** 10
old_sm = 10 ** 100
for x in range(13600, len(l)):
    sm = 0
    for y in l:
        if abs(l[x][0] - y[0]) > S / 2:
            sm += (S % abs(l[x][0] - y[0])) * (math.ceil(y[1] / 11))
        else:
            sm += abs(l[x][0] - y[0]) * (math.ceil(y[1] / 11))
    mn_sm = min(mn_sm, sm)
    if sm < old_sm:
        print(sm, '<<<<<<<<<<<<<<<<')
    else:
        print(sm, '>>>>>>>>>>>>>>>>')
    old_sm = sm
print(mn_sm)
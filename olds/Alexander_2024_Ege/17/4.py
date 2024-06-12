lx = 4444
lx1 = 22
lx2 = 22
l = [lx, lx1, lx2]
g = list(map(lambda h: len(str(h)), l))
if g.count(2) == 1:
    print('только число 1 двухзн..')
def tr(x, y, z):
    l = sorted([x, y, z])
    if l[2] < l[0] + l[1]:
        return True
    else:
        return False
for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((not(tr(x, 11, 18) == ((max(x, 5) <= 68)) and tr(x, A, 5)))) == 0:
            can = False
    if can:
        print(A)
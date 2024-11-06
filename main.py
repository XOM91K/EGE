def tr(a, b, c):
    l = sorted([a, b, c])
    if l[-1] < l[0] + l[1]:
        return 1
    return 0


for A in range(1, 1_000):
    can = True
    for x in range(1, 1000):
        if not ((tr(x, 11, 16) == (not (max(x, 5) > 10))) and (tr(4, A, x))) == 0:
            can = False
            break
    if can:
        print(A)

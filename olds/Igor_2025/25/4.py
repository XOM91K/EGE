def get_somn(n):
    ls = []
    for x in range(2, int(n ** 0.5) + 1):
        ls.append([x, n // x])
    return ls
for x in range(705460  , 705460   + 1):
    ls = get_somn(x)
    mx_rzn = abs(ls[0][0] - ls[0][1])
    mn_rzn = 10 ** 10
    for i in ls:
        if abs(i[0] - i[1]) > 4444:
            mn_rzn = min(mn_rzn, abs(i[0] - i[1]))
    print(x, mx_rzn, mn_rzn)
    if len(ls) >= 2 and mx_rzn % mn_rzn == 0 and mn_rzn > 4444:
        print(x, mn_rzn)
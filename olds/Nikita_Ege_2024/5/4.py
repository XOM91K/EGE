def th(x):
    t = ""
    while x != 0:
        #t.append(x % 3)
        t = str((x % 3)) + t
        x = x // 3
    return t


mn = 9 ** 9

for N in range(11, 100000):
    r = th(N)
    if (r.count('0') + r.count('2')) % 2 == 0:
        r = "22" + r
    else:
        r = "11" + r
    if int(r, 3) > 100:
        mn = min(mn, int(r, 3))

print(mn)
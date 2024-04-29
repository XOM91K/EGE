def v17(n):
    s = []
    while n > 0:
        s.append(n % 17)
        n = n // 17
    return s[::-1]


x = 5 * (3**1917)+6*(2**1878)+7*(3**1870)-1991
a = v17(x)
print(a)
for x in range(0, 17):
    print(a.count(x))

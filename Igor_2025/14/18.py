def v_11(n):
    res = ''
    while n >0:
        i = n % 11
        if i == 10:
            res += 'A'
        else:
            res += str(i)
        n = n//11
    return res[::-1]


S = (11 ** 250) + (11**5) - 358123

for x in range(0, 100_000+1,3):
    n = S - x
    n = v_11(n)
    if n.count('A') == 248:
        print(x)
        break
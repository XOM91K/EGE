def deli(n, m):
    if n % m == 0:
        return 1
    return 0
for A in range(1, 10000):
    flag = True
    for x in range(1, 10000):
        if ((deli(x, 2) <= (not(deli(x, 13)))) or (x + A >= 1000)) == 0:
            flag = False
            break
    if flag:
        print(A)
        break
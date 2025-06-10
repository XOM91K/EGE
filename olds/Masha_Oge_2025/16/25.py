def dels(n):
    dls = []
    for x in range(1, n + 1):
        if n % x == 0:
            dls.append(x)
    return len(dls)
a = -1
while a != 0:
    a = int(input())
    if a % 2 == 0 and a % 5 == 0:
        if dels(a) == 10:
            print(a)
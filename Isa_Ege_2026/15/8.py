n=371300
for a in range(n, 1, -1):
    k=1
    for x in range(1, n + 1):
        if ((x % 780 == 0) <= (((x % a != 0) <= (x % 560 != 0)) or (x % 340 != 0))) == 0:
            k = 0
            break
    if k==1:
        print(a)
        break
d = 124_500
for A in range(d, 1, -1):
    can = True
    for x in range(1, d):
        if ((x % 512 == 0) <= ((x % A != 0) <= (x % 243 != 0))) == 0:
            can = False
            break
    if can:
        print(A)
        break
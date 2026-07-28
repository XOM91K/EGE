d = 160100
for a in range(d, 1, -1):
    can = True
    for x in range(1, d):
        if ((x % 256 == 0) <= ((x % a != 0) <= (x % 625 != 0))) == 0:
            can = False
            break
    if can:
        print(a)
        break

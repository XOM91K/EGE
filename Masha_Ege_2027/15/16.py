d = 36000
for a in range(d, 1, -1):
    can = True
    for x in range(1, d):
        if ((x % 465 == 0) <= ((x % a != 0) <= (x % 385 != 0))) == 0:
            can = False
            break
    if can:
        print(a)
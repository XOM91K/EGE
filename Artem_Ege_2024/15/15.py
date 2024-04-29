ct = 0
for A in range(1, 1001):
    k = True
    for x in range(1, 1001):
        if ((A % 9 == 0) and ((280 % x == 0) <= ((A % x != 0) <= (730 % x != 0)))) == 0:
            k = False
    if k:
        print(A)
        ct += 1
print(ct)
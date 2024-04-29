sm = 0
for A in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x % A != 0) <= ((x % 120 == 0) or (x % 180 != 0))) == 0:
            can = False
    if can:
        sm += A
print(sm)
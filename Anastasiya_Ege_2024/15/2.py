k = 0
for a in range(1, 1000):
    can = True
    for x in range(1, 1000):
        if ((x % 12 == 0) and (70 <= x <= 80) and (x % a != 0)) == 1:
            can = False
    if can:
        k += 1
        print(a)
print(k)
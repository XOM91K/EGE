ct = 0
for x in range(10, 100):
    if (x <= 81 and (x % 10) % 2 == 0) == 0:
        ct += 1
        print(x)
print(ct)
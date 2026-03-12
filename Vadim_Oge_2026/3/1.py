ct = 0
for x in range(10, 100):
    if ((x < 74) and (x % 2 != 0)) == 0:
        print(x)
        ct += 1
print(ct)
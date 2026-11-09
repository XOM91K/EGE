ct = 0
for x in range(10, 100):
    if ((not(x >= 74)) and (x % 2 == 0)) == 0:
        ct += 1
        print(x)
print(ct)
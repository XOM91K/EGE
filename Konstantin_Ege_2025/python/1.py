ct = 0
for x in range(10, 100):
    if x % 3 != 0 or x % 4 == 0:
        ct += 1
print(ct)
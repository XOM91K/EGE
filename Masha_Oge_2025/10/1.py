ct = 0
for x in range(1, 1000):
    if int('45', 16) <= x < int('136', 8):
        if x % 2 == 0:
            ct += 1
print(ct)
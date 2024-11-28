ct = 0
for x in range(10 ** 9, 1_789_456_124):
    if x % 16 in [12, 13, 14, 15] or x % 4 in [0, 1, 2, 3]:
        ct += 1
print(ct)
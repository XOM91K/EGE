n = int(input())
i1 = 1
i2 = 1
s = 0
for x in range(3, n + 1):
    s = i1 + i2
    i1 = i2
    i2 = s
print(s)
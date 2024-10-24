n = 4
m = 8
k = 3
l = []
t = [1, 2, 3]
i = 0
c = 1
ct = 0
for y in range(n):
    l.append([])
    for x in range(m):
        if t[i % k] == c:
            ct += 1
        i += 1
    i -= 1
print(ct)
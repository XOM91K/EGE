l = [int(x) for x in open(r'2.txt')]
k = 158
mx = 0
for x in range(len(l)):
    for y in range(len(l)):
        for z in range(len(l)):
            if abs(x - y) >= k and abs(x - z) >= k and abs(y - z) >= k:
                mx = max(mx, l[x] + l[y] + l[x])
print(mx)
l = [int(x) for x in open('27B_7603 (2).txt')]
mx1 = 0
mx2 = 0
print(l)
for x in range(len(l) - 1000_000):
    mx1 = max(mx1, l[x])
    mx2 = max(mx2, mx1 + l[x + 1000_000])
print(mx2)
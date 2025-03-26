# 397
l = [int(x) for x in open('4.txt')]
mn = min(l) ** 2
mn2 = []
for x in range(len(l) - 1):
    if (l[x] % 77) * (l[x + 1] % 77) == mn:
        mn2.append(l[x] * l[x + 1])
print(len(mn2), min(mn2))
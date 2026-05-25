import math
q = []
l = [int(d) for d in open('18.txt')]
for x in range(len(l) - 1):
    if math.gcd(l[x], l[x + 1]) == 1:
        if (l[x] % 2 == 0 and l[x + 1] % 2 != 0) or (l[x] % 2 != 0 and l[x + 1] % 2 == 0):
            q.append(l[x] + l[x + 1])
print(len(q), min(q))
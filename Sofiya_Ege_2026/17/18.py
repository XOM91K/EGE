l = [int(x) for x in open('18.txt')]
ans = []
d = [x for x in l if 999 < abs(x) < 10000 and x % 17 == 0]
for x in range(len(l) - 2):
    n1 = l[x]
    n2 = l[x + 1]
    n3 = l[x + 2]
    if (999 < abs(n1) < 10000 and abs(n1) % 100 == 27) + (999 < abs(n2) < 10000 and abs(n2) % 100 == 27) + (
            999 < abs(n3) < 10000 and abs(n3) % 100 == 27) >= 1:
        if (n1 ** 2 + n2 ** 2 + n3 ** 2) <= min(d) ** 2:
            ans.append(abs(n1) + abs(n2) + abs(n3))
print(len(ans), min(ans))

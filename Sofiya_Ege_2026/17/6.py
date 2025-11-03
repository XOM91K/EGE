a = [int(x) for x in open('6.txt')]
d = [x for x in a if abs(x) % 1000 == 151]
ans = []
sr = sum(d) / len(d)
for x in range(len(a) - 2):
    n1 = a[x]
    n2 = a[x + 1]
    n3 = a[x + 2]
    if 0 < (999 < abs(n1) < 10000) + (999 < abs(n2) < 10000) + (999 < abs(n3) < 10000) < 3:
        if (n1 > sr) and (n2 > sr) and (n3 > sr):
            if (n1 % 13 == 0) + (n2 % 13 == 0) + (n3 % 13 == 0) > (n1 % 7 == 0) + (n2 % 7 == 0) + (n3 % 7 == 0):
                ans.append(n1 + n2 + n3)
print(len(ans), min(ans))

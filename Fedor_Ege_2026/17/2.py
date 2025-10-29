l = [int(x) for x in open('2.txt')]
mn = min(l) ** 2
mn_pr = []
for x in range(len(l) - 1):
    if (l[x] % 77) * (l[x + 1] % 77) == mn:
        mn_pr.append(l[x] * l[x + 1])
print(len(mn_pr), min(mn_pr))
#https://examinf.ru/tasks/397
l = [int(x) for x in open('2.txt')]
mn = min(l) ** 2
ct = 0
mn_pr = []
for x in range(len(l) - 1):
    if (l[x] % 77) * (l[x + 1] % 77) == mn:
        ct += 1
        mn_pr.append(l[x] * l[x + 1])
print(ct, min(mn_pr))

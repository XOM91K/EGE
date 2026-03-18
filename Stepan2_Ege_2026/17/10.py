l = [int(x) for x in open('10.txt')]
mx3 = max(d for d in l if str(d)[-1] == '3')
mn3 = min(d for d in l if d % 3 == 0)
mn = []
for x in range(len(l) - 1):
    k = 0
    if l[x] >= mn3 and l[x] <= mx3:
        k += 1
    if l[x + 1] >= mn3 and l[x + 1] <= mx3:
        k += 1
    if k == 1:
        mn.append((l[x] ** 2) + (l[x + 1] ** 2))
print(len(mn), min(mn))
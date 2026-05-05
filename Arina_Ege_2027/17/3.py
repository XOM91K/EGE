l = [int(x) for x in open('3.txt')]
mn3 = min([i for i in l if i % 3 == 0])
mx3 = max([i for i in l if i % 10 == 3])
mn = []
for x in range(len(l) - 1):
    k = 0
    if l[x] >= mn3 and l[x] <= mx3:
        k += 1
    if l[x + 1] >= mn3 and l[x + 1] <= mx3:
        k += 1
    if k == 1:
        mn.append(l[x] ** 2 + l[x + 1] ** 2)
print(len(mn), min(mn))
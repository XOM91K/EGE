l = [int(x) for x in open('11.txt')]
sr = sum(l) / len(l)
mn = []
ll = []
for x in range(len(l) - 1):
    k = 0
    if l[x] > sr:
        k += 1
    if l[x + 1] > sr:
        k += 1
    if k == 1:
        if abs((l[x] + l[x + 1]) - (max(l) + min(l))) >= 1000:
            ll.append(l[x])
            ll.append(l[x + 1])
# print(len(mn), min(mn))
print(len(ll))
for x in range(len(l) - 1):
    for y in range(x + 1, len(l)):
        k = 0
        if l[x] > sr:
            k += 1
        if l[y] > sr:
            k += 1
        if k == 1:
            if abs((l[x] + l[y]) - (max(l) + min(l))) >= 1000:
                mn.append(l[x] + l[y])
print(len(mn), min(mn))
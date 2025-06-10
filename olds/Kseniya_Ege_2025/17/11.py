l = [int(x) for x in open('11.txt')]
mx2 = max([x for x in l if len(str(x)) == 2])
A = []
mn = []
for x in range(len(l) - 3):
    if str(l[x])[-1] == str(l[x + 1])[-1] == str(l[x + 2])[-1] == str(l[x + 3])[-1]:
        A.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3])
A = max(A)
for x in range(len(l) - 4):
    k = 0
    if l[x] < A:
        k += 1
    if l[x + 1] < A:
        k += 1
    if l[x + 2] < A:
        k += 1
    if l[x + 3] < A:
        k += 1
    if l[x + 4] < A:
        k += 1
    if k == 1:
        if (l[x] + l[x + 1] + l[x + 2] + l[x + 3] + l[x + 4]) % mx2 == 0:
            mn.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3] + l[x + 4])
print(len(mn), min(mn))
l = [int(x) for x in open('3.txt')]
mx2 = max([x for x in l if len(str(abs(x))) == 2])
A = []
for x in range(len(l) - 3):
    if abs(l[x]) % 10 == abs(l[x + 1]) % 10 == abs(l[x + 2]) % 10 == abs(l[x + 3]) % 10:
        A.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3])
A = max(A)
mx = []
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
            print(1)
            mx.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3] + l[x + 4])
print(len(mx), min(mx))
l = [int(x) for x in open("22.txt")]
ct = 0
A = -10000000
mn = 10 ** 10
mx1 = max([x for x in l if len(str(abs(x))) == 2])
for x in range(len(l) - 3):
    v = str(l[x])
    b = str(l[x + 1])
    c = str(l[x + 2])
    d = str(l[x + 3])
    if v[-1] == b[-1] == c[-1] == d[-1]:
        v = int(l[x])
        b = int(l[x + 1])
        c = int(l[x + 2])
        d = int(l[x + 3])
        A = max(A, v + b + c + d)
print(A)
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
    if k == 1 and (l[x] + l[x + 1] + l[x + 2] + l[x + 3] + l[x + 4]) % mx1 == 0:
        mn = min(mn, l[x] + l[x + 1] + l[x + 2] + l[x + 3] + l[x + 4])
        ct += 1

print(ct, mn)
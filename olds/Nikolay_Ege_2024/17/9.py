l = [int(x) for x in open('9.txt')]
mx_2 = 0
A = -10**7
for x in l:
    if len(str(abs(x))) == 2:
        mx_2 = max(mx_2, x)
for x in range(len(l) - 3):
    if abs(l[x]) % 10 == abs(l[x + 1]) % 10 == abs(l[x + 2]) % 10 == abs(l[x + 3]) % 10:
        A = max(A, l[x] + l[x + 1] + l[x + 2] + l[x + 3])
ct = 0
mn = 10 ** 10
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
    if k == 1 and (l[x] + l[x + 1] + l[x + 2] + l[x + 3] + l[x + 4]) % mx_2 == 0:
        ct += 1
        mn = min(mn, l[x] + l[x + 1] + l[x + 2] + l[x + 3] + l[x + 4])

print(ct, mn)
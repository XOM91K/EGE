l = [int(x) for x in open('1')]
A = -100000000
mx2 = 0
for x in range(len(l) - 3):
    if str(l[x])[-1] == str(l[x + 1])[-1] == str(l[x + 2])[-1] == str(l[x + 3])[-1]:
        A = max(A, l[x] + l[x + 1] + l[x + 2] + l[x +3])
for x in l:
    if len(str(x)) == 2:
        mx2 = max(mx2, x)
ct5 = 0
mn_sm = 1000000000
for x in range(len(l) - 4):
    ct = 0
    if l[x] < A:
        ct += 1
    if l[x + 1] < A:
        ct += 1
    if l[x + 2] < A:
        ct += 1
    if l[x + 3] < A:
        ct += 1
    if l[x + 4] < A:
        ct += 1
    if ct == 1 and (l[x] + l[x + 1] + l[x + 2] + l[x + 3] + l[x + 4]) % mx2 == 0:
        ct5 += 1
        mn_sm = min(mn_sm, l[x] + l[x + 1] + l[x + 2] + l[x + 3] + l[x + 4])

print(ct5, mn_sm)
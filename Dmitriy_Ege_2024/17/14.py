l = [int(x) for x in open('14.txt')]
A = -10 ** 7
ct = 0
mx_dv = []
mn_sum_otv = []
for x in l:
    if len(str(abs(x))) == 2:
        mx_dv.append(x)
mx_dv = max(mx_dv)
for x in range(len(l) - 3):
        if str(l[x])[-1] == str(l[x + 1])[-1] == str(l[x + 2])[-1] == str(l[x + 3])[-1]:
            A = max(A, l[x] + l[x + 1] + l[x + 2] + l[x + 3])
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
        if (l[x] + l[x + 1] + l[x + 2] + l[x + 3] + l[x + 4]) % mx_dv == 0:
            ct += 1
            mn_sum_otv.append(l[x] + l[x + 1] + l[x + 2] + l[x + 3] + l[x + 4])
print(ct, min(mn_sum_otv))
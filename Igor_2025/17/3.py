l = [int(x) for x in open('3.txt')]
ct = 0
mn = 10 ** 10
mx2 = max([d for d in l if len(str(abs(d))) == 2])
A = -10 ** 101
for x in range(len(l) - 3):
    if str(abs(l[x]))[-1] == str(abs(l[x + 1]))[-1] == str(abs(l[x + 2]))[-1] == str(abs(l[x + 3]))[-1]:
        A = max(A, l[x] + l[x + 1] + l[x + 2] + l[x + 3])

for x in range(len(l) - 4):
    k = 0
    sm5 = 0
    for y in range(5):
        sm5 += l[x + y]
        if l[x + y] < A:
            k += 1
    if k == 1 and sm5 % mx2 == 0:
        ct += 1
        mn = min(mn, sm5)

print(ct, mn)
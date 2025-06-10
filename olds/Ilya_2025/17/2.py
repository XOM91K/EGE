l = [int(x) for x in open('2.txt')]
A = -10**7
for x in range(len(l) - 3):
    if abs(l[x]) % 10 == abs(l[x + 1]) % 10 == abs(l[x + 2]) % 10 == abs(l[x + 3]) % 10:
        A = max(A, l[x] + l[x + 1] + l[x + 2] + l[x + 3])
mx2 = max([d for d in l if len(str(abs(d))) == 2])
ct = 0
mn = 10 ** 10
for x in range(len(l) - 4):
    k = 0
    sm = 0
    for y in range(5):
        if l[x + y] < A:
            k += 1
            sm += l[x + y]
    if k == 1 and sm % mx2 == 0:
        print(l[x], l[x + 1], l[x + 2], l[x + 3], l[x + 4])
        mn = min(mn, sm)
        ct += 1
print(ct, mn)
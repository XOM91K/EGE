l = [[int(d) for d in x.split()] for x in open('13.txt')]
ct = 0
for x in l:
    k = 0
    if x == sorted(x)[::-1]:
        k += 1
    if min(x) < 5:
        k += 1
    if max(x) > 50:
        k += 1
    if k == 2:
        ct += 1
print(ct)
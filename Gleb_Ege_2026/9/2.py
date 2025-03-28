l = [[int(d) for d in x.split()] for x in open('2.txt')]
ct = 0
for x in l:
    ch = [d for d in x if d % 2 == 0]
    nch = [d for d in x if d % 2 != 0]
    k = 0
    if len(set(x)) == 4:
        k += 1
    if sum(nch) > sum(ch):
        k += 1
    if k == 1:
        ct += 1
print(ct)

# l = [x for x in range(5, 51) if x % 2 == 0]
# print(l)
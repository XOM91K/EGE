l = [sorted([int(d) for d in x.split()]) for x in open("3.txt")]
ct = 0
for x in l:
    k = 0
    if len(set(x)) == 4:
        k += 1
    if sum(d for d in x if d % 2 != 0) > sum(d for d in x if d % 2 == 0):
        k += 1
    if k == 1:
        ct += 1
print(ct)


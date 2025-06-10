cnt = 0
l = [[int(d) for d in x.split()] for x in open('1.txt')]
ct = 0
for x in l:
    k = 0
    if x == sorted(x):
        k += 1
    x.sort()
    if len(set(x)) == 5 and (x.count(x[2]) == 3 or x.count(x[4]) == 3):
        k += 1
    if k <= 1:
        ct += 1
print(ct)
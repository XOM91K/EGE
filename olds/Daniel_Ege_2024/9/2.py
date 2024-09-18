l = [[int(d) for d in x.split()] for x in open('2.txt')]
ct = 0
for x in l:
    k = 0
    if x[0] > sum(x) / len(x):
        k += 1
    if x[1] > sum(x) / len(x):
        k += 1
    if x[2] > sum(x) / len(x):
        k += 1
    if x[3] > sum(x) / len(x):
        k += 1
    if x[4] > sum(x) / len(x):
        k += 1
    if k >= 3:
        ct += 1
print(ct)
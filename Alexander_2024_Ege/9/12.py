l = [[int(d) for d in x.split()] for x in open('12.txt')]
ct = 0
for x in l:
    x.sort()
    if x[-2] - 20 == x[1]:
        ct += 1
print(ct)
l = [[int(d) for d in x.split()] for x in open('6.txt')]
k = 0
ct = 0
for x in l:
    k += 1
    if len(set(x)) == 5:
        x.sort()
        if x[-1] - x[0] == x[1] + x[2] + x[3]:
            print(k)
            ct += 1
print(ct)
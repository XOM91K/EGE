l = [sorted([int(d) for d in x.split()])for x in open('15.txt')]
ct = 0
for x in l:
    if x[0] == x[1] and x[2] == x[3]:
        print(x)
        if (x[1] + x[2]) % x[0] == 0:
            ct += 1
print(ct)
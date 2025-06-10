l = [sorted([int(d) for d in x.split()]) for x in open('14.txt')]
ct = 0

for x in l:
    chet = []
    nech = []
    if x[3] < (x[0]+x[1]+x[2]):
        for y in x:
            if y % 2 == 0:
                chet.append(y)
            else:
                nech.append(y)
        if sum(chet) == sum(nech):
            ct += 1
print(ct)
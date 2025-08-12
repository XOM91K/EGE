l = [[int(d) for d in x.split()] for x in open('316.txt')]
ct = 0
for x in l :
    x=sorted(x)
    if x[-1]<x[0]+x[1]+x[2]:
        if x[0] + x[-1] == x[1] + x[2]:
            ct += 1
print(ct)
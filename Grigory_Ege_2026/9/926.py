l = [[int(d) for d in x.split()] for x in open('926.txt')]
ct=0
for x in l :
    x = sorted(x)
    cht = [y for y in x if y % 2 == 0]
    ncht = [y for y in x if y % 2 != 0]
    if x[-1] < x[0] + x[1]+ x[2]:
        if sum(cht) == sum(ncht):
            ct +=1
print(ct)
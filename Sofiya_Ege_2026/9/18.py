import itertools
l=[[int(d)for d in x.split()]for x in open('18.txt')]
d=[]
for x in l:
    x=sorted(x)
    # 8 9 6 4 8 9 6 2 => 2 4 6 6 8 8 9 9
    can = 0
    for y in itertools.combinations(x, 6):
        if y[0] == y[1] and y[2] == y[3] and y[4] == y[5]:
            can = 1
            break
    if (x[0]**2 in x)+can==1:
        d.append(sum(x))
print(min(d))
# import itertools
# for x in itertools.combinations(sorted('89648962'), 6):
#     print(x)
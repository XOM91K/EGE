l = [[int(d) for d in x.split()] for x in open('15.txt')]
for x in l:
    povt=[]
    x.sort()
    for y in x:
        if x.count(y) == 2:
            povt.append(y)
    if len(povt)==4 and x[-1]!=x[-2] and (x[0]*x[-1]>(x[1]+x[2]+x[3]+x[4])):
        print(x, sum(x))
        break
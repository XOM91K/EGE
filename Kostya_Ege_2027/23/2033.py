l = [[d for d in x.split()] for x in open('2033.txt')]
for x in range(len(l)):
    l[x] = [int(l[x][0]),int(l[x][1]),float(l[x][2])]
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append([x[1],x[2]])

def f(x,y):
    if x == y:
        return 0
    if x not in sl:
        return -float('inf')
    vars = []
    for z in sl[x]:
        vars.append(z[1] + f(z[0],y))
    return max(vars)
print(f(12,89))
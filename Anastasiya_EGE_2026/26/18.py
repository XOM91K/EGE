l = [[int(d) for d in x.split()] for x in open('18.txt')]
k = 3
lines = []
can = True
print(l)
for x in l:
    if can:
        lines.append([0] * 3)
        can = False
    canClient = True
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (x[0] - lines[i][j]) >= 1:
                if canClient == False:
                    lines[i][j] = 0
                if canClient:
                    lines[i][j] = x[1]
                    print(x)
                    canClient = False
    if len([d for d in lines[-1] if d > 0]) == 3:
        can = True
print(len(lines), lines[-1], lines[-2])
ct = 0
for x in lines:
    for y in x:
        if y > 691:
            ct +=1
print(ct)
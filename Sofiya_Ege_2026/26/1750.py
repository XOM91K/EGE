l=[g.replace('R','1').replace('G','2').replace('B','3').split() for g in open('1750.txt')]
for f in range(len(l)):
    l[f] = [int(l[f][0]), int(l[f][1]), int(l[f][2])]
print(l)
l = sorted(l, key=lambda d: (-d[1], d[0]))
x = 0
can = True
bashni = []
while len(l) > 0:
    if x >= len(l):
        break
    if can:
        for i in range(len(l)):
            if l[i][-1] == 1:
                bashni.append([l[i]])
                del l[i]
                can = False
                break
        else:
            exit()
    else:
        if l[x][-1] - bashni[-1][-1][-1] == 1 and bashni[-1][-1][1] - l[x][1] >= 2  and len(bashni[-1]) < 3:
            bashni[-1].append(l[x])
            del l[x]
        elif len(bashni[-1]) == 3:
            can = True
            x = 0
        elif l[x][-1] - bashni[-1][-1][-1] != 1 or bashni[-1][-1][1] - l[x][1] < 2:
            x += 1
print(len(bashni))
print(bashni[-1])
# bashni = [ [5, 4, 1], [10, 5, 1], [10, 5, 1],[10, 5, 1],[10, 5, 1],[10, 5, 1],[10, 5, 1],[10, 5, 1],]
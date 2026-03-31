l = [[int(d) for d in x.split()] for x in open('9.txt')]
mesta = [-1] * 997
new_l = []
for x in l:
    new_l.append(x[0])
    new_l.append(x[1])
new_l = sorted(new_l)
i = 0
j = -1
# 4, 1, 2, 3, 5
rasm = []
for x in new_l:
    if x not in rasm:
        for y in range(len(l)):
                if x == l[y][0]:
                    rasm.append(l[y][0])
                    rasm.append(l[y][1])
                    print(y + 1)
                    mesta[i] = y + 1
                    i += 1
                    break
                elif x == l[y][1]:
                    rasm.append(l[y][0])
                    rasm.append(l[y][1])
                    print(y + 1)
                    mesta[j] = y + 1
                    j -= 1
                    break
print(mesta)
print(mesta.index(895))
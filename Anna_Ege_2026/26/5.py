l = [int(x) for x in open('5.txt')]
l = sorted(l)[::-1]
i = 0
cont = []
can = True
while len(l) > 0:
    if i == len(l):
        can = True
        i = 0
    if can:
        cont.append([l[i]])
        del l[i]
        can = False
    else:
        if cont[-1][-1] - l[i] >= 9:
            cont[-1].append(l[i])
            del l[i]
        else:
            i += 1
print(l)

print(len(max(cont, key=len)), len(cont))
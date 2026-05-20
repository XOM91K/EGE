l = [[int(d) for d in x.split()] for x in open('1751.txt')]
l = sorted(l, key=lambda d: (-d[-1], d[0]))
bash = []
can = True
i = 0
while len(l) > 0:
    if i == len(l):
        i = 0
        can = True
    if can:
        bash.append([l[0]])
        del l[0]
        can = False
    else:
        if bash[-1][-1][1] - l[i][1] >= 2:
            bash[-1].append(l[i])
            del l[i]
        else:
            i += 1


print([len(d) for d in bash])
print(bash[-1], bash[-2])
print(980 + 810 + 659)
print(sum([d[-1][0] for d in bash]))
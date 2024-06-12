l = sorted([int(x) for x in open('11.txt')], reverse=True)
i = 0
r = []
flag = True
while len(l) != 0:
    if flag:
        r.append([l[i]])
        del l[i]
        i -= 1
        flag = False
    elif abs(r[-1][-1] - l[i]) >= 9:
        r[-1].append(l[i])
        del l[i]
        i -= 1
    if i == len(l) - 1:
        flag = True
        i = -1
    i += 1
print(len(r), len(max(r, key=len)))
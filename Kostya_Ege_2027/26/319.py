l = [int(x) for x in open('319.txt')]
l = sorted(l)[::-1]
i = 0
flag = True
torts = []
while len(l) != 0:
    if flag:
        torts.append([l[i]])
        del l[i]
        flag = False
    if len(l) == 0:
        break
    if torts[-1][-1] - l[i] >= 9:
        torts[-1].append(l[i])
        del l[i]
        if i == len(l):
            i = 0
            flag = True
    else:
        i += 1
        if i == len(l):
            flag = True
            i = 0
print(len(torts), len(max(torts, key=len)))
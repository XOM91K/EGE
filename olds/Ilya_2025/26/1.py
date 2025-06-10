s = 8200
d = s
l = sorted([int(x) for x in open('1.txt')])
l_new = []
i = 0
while s - l[i] > 0:
    s -= l[i]
    l_new.append(l[i])
    i += 1
print(len(l_new))
del l_new[-1]
for x in range(len(l) - 1, -1, -1):
    if sum(l_new) + l[x] <= d:
        print(l[x])
        break
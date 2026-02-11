l = [[int(d) for d in x.split()] for x in open('8.txt')]
l = sorted(l)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
print(sl)
mx_ct = 1
for x in sl:
    ct = 1
    sl[x] = sorted(set(sl[x]))
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            ct += 1
            mx_ct = max(mx_ct, ct)
        else:
            ct = 1
print(mx_ct)
for x in sl:
    ct = 1
    sl[x] = sorted(set(sl[x]))
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            ct += 1
            if ct == 148:
                print(x)
        else:
            ct = 1
# sl = {'red': 500, 5: -120}
# print(sl[5])
# print(sl['red'])
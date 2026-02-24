l = [[int(d) for d in x.split()] for x in open('16.txt')]
l = sorted(l)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])

# print(sl)
mx_ct = 1
mx=[]
for x in sl:
    sl[x] = sorted(set(sl[x]))
    ct = 1
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            ct += 1
            if ct == 148:
                print(x)
                exit()
            mx_ct = max(mx_ct, ct)
            mx.append(sl[x])
        else:
            ct = 1
print(mx_ct)
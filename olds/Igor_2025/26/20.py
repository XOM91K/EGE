l = [[int(d) for d in x.split()] for x in open('20.txt')]
l.sort()
print(l)
z = []
for x in l:
    z.append(x[0])
    z.append(x[1])
z = sorted(set(z))
sl = {}
for i in z:
    sl[i] = 0
for x in l:
    sl[x[0]] = sl[x[0]] + 1
    sl[x[1]] = sl[x[1]] - 1
rast = 0
flag = 0
for i in range(len(z) - 1):
    if not flag:
        st = sl[z[i]]
    if sl[z[i + 1]] != 0:
        ed = sl[z[i + 1]]
        rast = max(rast, abs(z[i + 1] - z[i]))
        flag = 0
    else:
        flag = 1

print(sl, rast)
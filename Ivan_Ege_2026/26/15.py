a = [[int(d) for d in x.split()] for x in open('15.txt')]
a = sorted(a)
sl = {}
for e in a:
    if e[0] not in sl:
        sl[e[0]] = []
    sl[e[0]].append(e[1])
for e in sl:
    sl[e] = sorted(set(sl[e]))
cm = 1
for e in sl:
    c = 1
    sl[e].append(0)
    for i in range(len(sl[e])-2):
        if sl[e][i+1]-sl[e][i] == 2:
            c += 1
            if c >= cm:
                cm = c
                sl[e][-1] = cm
        else:
            c = 1
print(cm)
for e in sl:
    if sl[e][-1] == 42:
        print(e)
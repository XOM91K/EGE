l = [int(x) for x in open('32.txt')]
l = sorted(l)
gr = []
rz = []
for x in l:
    if 310 <= x <= 320:
        rz.append(x)
for x in l:
    sv = 10000 - sum(rz) - sum(gr)
    if not(310 <= x <= 320) and sum(gr) + x <= (10000 - sum(rz)):
        gr.append(x)
sv = 10000 - sum(rz) - sum(gr)
i = -1
l = l[::-1]
dobav = []
while abs(i) <= len(gr):
    sv += gr[i]
    del gr[i]
    for x in range(len(l)):
        if not(310 <= l[x] <= 320) and x not in dobav:
            if sv - l[x] >= 0:
                sv -= l[x]
                gr.append(l[x])
                dobav.append(x)
                i -= 1
                break
print(gr, rz)
print((sum(gr)) + sum(rz), len(gr) + len(rz))

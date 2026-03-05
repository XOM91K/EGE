l = [[d for d in x.split()] for x in open('9.txt')]
l = sorted(l)
sl = {}
for x in l:
    if int(x[0]) not in sl:
        sl[int(x[0])] = []
    sl[int(x[0])].append([int(x[1]), x[2]])
ct = 0
mx_ct = 0
for x in sl:
    mx_ct_line = 0
    for i in range(6, len(sl[x])):
        if sl[x][i][1] ==  sl[x][i - 1][1] ==  sl[x][i - 2][1] ==  sl[x][i - 4][1] ==  sl[x][i - 5][1] ==  sl[x][i -6][1] == '#0000FF' and sl[x][i - 3][1] == '#00FF00':
            ct += 1
            mx_ct_line += 1
    if mx_ct_line > mx_ct:
        mx_ct = mx_ct_line
    if mx_ct_line == 2:
        print(x)

print(ct, mx_ct)

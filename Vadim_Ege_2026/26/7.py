l = [[int(d) for d in x.split()] for x in open('7.txt')]
l = sorted(l)
sl = {}
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
mx_lines = []
for x in sl:
    sl[x] = sorted(set(sl[x]))
    K = 1
    sl[x].append(10 ** 6)
    lines = 0
    for y in range(len(sl[x]) - 1):
        if sl[x][y + 1] - sl[x][y] == 1:
            K += 1
        else:
            if K >= 5:
                lines += 1
                if lines == 9:
                    print(x)
            K = 1
    mx_lines.append(lines)
print(max(mx_lines))
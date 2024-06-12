l = sorted([[int(d) for d in x.split()] for x in open('26.txt')])
k = 120
cells = [0 for x in range(k)]
times_busy = 0
ct_leave = 0
for x in l:
    for y in range(len(cells)):
        if x[0] > cells[y]:
            cells[y] = sum(x)
            break
    else:
        ct_leave += 1
print(ct_leave)

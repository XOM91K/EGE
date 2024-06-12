#kompege 7626
l = sorted([[int(d) for d in x.split()] for x in open('3.txt')])
cells = [0] * 210
ct = 0
last_passenger = 0
for x in l:
    for y in range(len(cells)):
        if x[0] > cells[y]:
            cells[y] = x[1]
            last_passenger = y
            ct += 1
            break
print(ct, last_passenger + 1)

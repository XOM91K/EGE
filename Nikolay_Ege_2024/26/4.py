l = sorted([[int(d) for d in x.split()] for x in open('4.txt')])
ct_passenger = 0
last_ind = 0
cells = [0] * 210
for x in l:
    for y in range(len(cells)):
        if x[0] >= cells[y]:
            cells[y] = x[1] + 1
            last_ind = y
            ct_passenger += 1
            break
print(ct_passenger, last_ind + 1)
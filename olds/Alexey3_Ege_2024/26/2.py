#8512
l = [[int(d) for d in x.split()] for x in open('2.txt')]
l = sorted(l)
cells = [0] * 210
ct = 0
for x in l:
    for y in range(len(cells)):
        if x[0] > cells[y]:
            cells[y] = x[1]
            ct += 1
            print(y + 1)
            break
print(ct)
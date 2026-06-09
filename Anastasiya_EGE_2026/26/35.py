l = sorted([[int(d) for d in x.split()] for x in open('35.txt')])
computers = []
for y in range(100):
    computers.append([0, 0])
ct = 0
for x in l:
    for y in range(len(computers)):
        if x[0] > computers[y][0]:
            computers[y][0] = x[1]
            computers[y][1] += (x[1] - x[0]) * ((x[1] - x[0]) + 1) // 2
            ct += 1
            break
print(ct, max([d[1] for d in computers]))
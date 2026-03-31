l = [[int(d) for d in x.split()] for x in open('22.txt')]
l = sorted(l, key=lambda d: d[0])
sl = {}
seats = ['1'] * 6661
for x in l:
    if x[0] not in sl:
        sl[x[0]] = []
    sl[x[0]].append(x[1])
for x in sl:
    for y in sl[x]:
        seats[y - 1] = '0'
    seats2 = ''.join(seats)
    if '11' in seats2:
        print(x, seats2.index('11') + 1)
    if '11' not in seats2:
        print(x)
        break

l = [[int(d) for d in x.split()] for x in open('33.txt')]
mins = [0] * 1440
for x in l:
    for y in range(x[0], x[1] + 1):
        mins[y] += 1
for y in range(len(mins)):
    mins[y] = [y, mins[y]]
mx_ct = []
ct = 1
for y in range(len(mins) - 1):
    if mins[y][1] == mins[y + 1][1]:
        ct += 1
        mx_ct.append(ct)
    else:
        ct = 1
print(max(mx_ct))
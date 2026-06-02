l = [[int(d) for d in x.split()] for x in open('18.txt')]
mins = [0] * 1440
print(mins)
for x in l:
    for y in range(x[0], x[1] + 1):
        mins[y] += 1
mx_ct = []
ct = 1
for x in range(len(mins) - 1):
    if mins[x] == mins[x + 1]:
        ct += 1
        mx_ct.append(ct)
    if mins[x] != mins[x + 1]:
        ct = 1
        print(x + 1)
print(mins)
print(max(mx_ct))
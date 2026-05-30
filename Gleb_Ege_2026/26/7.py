l = [[int(d) for d in x.split()] for x in open('7.txt')]
mins = [0] * 1441
for x in l:
    for y in range(x[0] - 1, x[1]):
        mins[y] += 1
ct = 1
mx_ct = []
for x in range(len(mins) - 1):
    if mins[x + 1] == mins[x]:
        ct += 1
        mx_ct.append(ct)
    if mins[x + 1] != mins[x]:
        print(x + 2)
        ct = 1
print(max(mx_ct))
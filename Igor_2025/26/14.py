l = [[int(d) for d in x.split()] for x in open('14.txt')]
l = sorted(l, key=lambda d: d[1])
time_finished = 0
mer = []
for x in l:
    if x[0] - time_finished >= 15:
        time_finished = x[1]
        mer.append(x)
print(len(mer), mer[-1][0] - mer[-2][1])
mx = 0
can = False
for y in l:
    if y == mer[-1]:
        can = True
    if can:
        mx = max(mx, y[0])
print(mx - mer[-2][1])
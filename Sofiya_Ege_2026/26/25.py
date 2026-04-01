d = 1236147000
l = [[int(d) for d in x.split()] for x in open('25.txt')]
mx = max(max(l, key=max))
time = [0] * (mx - d)
for x in range(len(time)):
    for y in l:
        if y[0] <= x + d < y[1] or (y[0] == 0 and x + d < y[1]) or (y[1] == 0 and x + d >= y[0]) or (y[0] == 0 and y[1] == 0):
            time[x] += 1
print(max(time))
ct = 0
for x in time:
    if x == 5:
        ct += 1
print(ct)
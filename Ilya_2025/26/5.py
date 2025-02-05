l = [[int(d) for d in x.split()] for x in open('5.txt')]
#print(max(l, key=lambda d: d[1])[1])
time = [0 for x in range(1440)]
for x in range(len(time)):
    for y in l:
        if y[0] <= x <= y[1]:
            time[x] += 1
piks = 0
can = False
#444444442
for x in range(len(time) - 1):
    if time[x] == max(time) and time[x + 1] != max(time):
        piks += 1
print(piks, max(time))
#4444 44444
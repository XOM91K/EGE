l = [[int(d) for d in x.split()] for x in open('23.txt')]
minutes = [0] * 1440
for x in range(len(minutes)):
    for y in l:
        if y[0] <= x <= y[1]:
            minutes[x] += 1
print(max(minutes))
print(minutes)
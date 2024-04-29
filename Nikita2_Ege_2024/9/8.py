l = [sorted([int(d) for d in x.split()]) for x in open('8.txt')]
k = 0
sm = 0
ct = 0
sr = 0
for x in l:
    k += 1
    if len(set(x)) == 5:
        if x[0] * x[1] * 2 <= x[2] + x[3] + x[4]:
            ct += 1
            sm += k
sr = sm / ct
print(sr)
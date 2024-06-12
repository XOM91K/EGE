l = sorted([[int(d) for d in x.split()] for x in open('3.txt')])
r = [0] * 210
ct = 0
last_pas = 0
for x in l:
    for y in range(len(r)):
        if x[0] > r[y]:
            r[y] = x[1]
            ct += 1
            last_pas = y + 1
            break
print(ct, last_pas)
l = [int(x) for x in open('4.txt')]
minn = min(l)
ct = 0
sm = []
for x in range(len(l) - 1):
    if (l[x]%77) * (l[x+1]%77) == minn ** 2:
        ct += 1
        sm.append(l[x]*l[x+1])
print(ct,min(sm))
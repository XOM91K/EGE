l = [int(x) for x in open('16.txt')]
l = sorted(l)
sm = 99187
i = 0
while sm - l[i] >= 0:
    sm -= l[i]
    i += 1
print(len(l) - i, sm)
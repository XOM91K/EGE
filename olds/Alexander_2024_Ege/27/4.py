import math
l = sorted([[int(d) for d in x.split()] for x in open('4.txt')])
for x in range(len(l)):
    l[x] = [l[x][0], math.ceil(l[x][1] / 48)]
mn = 10 ** 10
sm = 10 ** 10
for i in range(49900, len(l)):
    ct = 0
    for j in range(len(l)):
        ct += abs(l[i][0] - l[j][0]) * l[j][1]
    if ct < sm:
        print('>>>>>>>>', ct, l[i][0])
    else:
        print('<<<<<<<<', ct, l[i][0])
    sm = ct
    mn = min(mn, ct)

print(mn)
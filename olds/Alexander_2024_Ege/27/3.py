K = 60
R = 1
T = 40
l = [[int(d) for d in x.split()] for x in open('3.txt')]
for i in range(len(l)):
    ct = 0
    for j in range(len(l)):
        if K - abs(l[j][0] - l[i][0]) > T:
            ct += l[j][1]
    print(ct)
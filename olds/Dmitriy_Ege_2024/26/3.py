l = sorted([int(x) for x in open('3.txt')])
d = sorted([int(x) for x in open('3.txt')])
d_new = []
i = -1
j = 0
k = 1
while len(d_new) != len(d):
    if k % 4 != 0:
        d_new.append(d[i])
    else:
        d_new.append(d[j])
        j += 1
        i += 1
    i -= 1
    k += 1
sm = 0
for x in range(len(d_new)):
    if (x + 1) % 4 == 0:
        sm += d_new[x] / 2
    else:
        sm += d_new[x]
print(sm)
#39434611

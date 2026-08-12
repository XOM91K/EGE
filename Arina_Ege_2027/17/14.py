l = [int(x) for x in open("14.txt")]
mx = []
sm = 0
for i in range(len(l) - 2):
    k = 0
    if abs(l[i]) % 40 == 15:
        k += 1
    if abs(l[i + 1]) % 40 == 15:
        k += 1
    if abs(l[i + 2]) % 40 == 15:
        k += 1
    if k == 2:
        o = 0
        if abs(l[i]) % 7 == 0:
            o += 1
        if abs(l[i + 1]) % 7 == 0:
            o += 1
        if abs(l[i + 2]) % 7 == 0:
            o += 1
        if o <= 2:
            mx.append(l[i])
            if abs(l[i]) % 40 != 15:
                sm += l[i]
            if abs(l[i + 1]) % 40 != 15:
                sm += l[i + 1]
            if abs(l[i + 2]) % 40 != 15:
                sm += l[i + 2]
print(len(mx), sm)

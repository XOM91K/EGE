l = [int(x) for x in open('3.txt')]
mx = []
sr = 0
c = 0
for e in l:
    if abs(e)%100 == 28:
        sr += e
        c += 1
sr = sr/c
for i in range(len(l) - 2):
    if len(str(abs(l[i])))==4 or len(str(abs(l[i+1])))==4 or len(str(abs(l[i+2])))==4:
        c = 0
        if abs(l[i])%100 == 11:
            c += 1
        if abs(l[i+1])%100 == 11:
            c += 1
        if abs(l[i+2])%100 == 11:
            c += 1
        if c == 2:
            if l[i] > sr and l[i+1] > sr and l[i+2] > sr:
                mx.append(l[i]+l[i+1]+l[i+2])
print(len(mx), min(mx))
l = [int(x) for x in open('10.txt')]
mx = 0
otv = 0
trmx = 0
for i in range(len(l)):
    l[i] = int(l[i])
    if str(l[i])[-2:] == "15":
        mx = max(mx, l[i])
for i in range(len(l)-2):
    chet = 0
    for j in range(3):
        if l[i+j] >= 1000 and l[i+j] < 10000:
            chet += 1
    if (chet == 1) and (l[i]+l[i+1]+l[i+2] >= mx):
        otv += 1
        trmx = max(trmx, l[i]+l[i+1]+l[i+2])
print(otv, trmx)
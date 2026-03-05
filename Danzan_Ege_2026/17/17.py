l = [int(x) for x in open('17.txt')]
mx69 = (max([x for x in l if str(x)[-2:] == '69']))**2
min17 = sorted([x for x in l if x > 0 and x % 17 == 0])
sm17 = min17[0] + min17[1]
mn = []
for x in range(len(l) - 3):
    k = 0
    k2 = 0
    if l[x] % 18 == 0:
        k+=1
    if l[x + 1] % 18 == 0:
        k+=1
    if l[x + 2] % 18 == 0:
        k+=1
    if l[x + 3] % 18 == 0:
        k+=1
    if len(str(abs(l[x]))) == 3:
        k2+=1
    if len(str(abs(l[x + 1]))) == 3:
        k2+=1
    if len(str(abs(l[x + 2]))) == 3:
        k2+=1
    if len(str(abs(l[x + 3]))) == 3:
        k2+=1
    if k == 1 and k2 == 2:
        if (l[x] + l[x + 1] + l[x + 2] + l[x + 3]) % sm17 == 0:
            if (l[x] * l[x + 1] * l[x + 2] * l[x + 3]) <= mx69:
                mn.append((l[x] + l[x + 1] + l[x + 2] + l[x + 3])**2)
print(len(mn), min(mn))
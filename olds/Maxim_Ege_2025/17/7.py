l = [int(x) for x in open('7.txt')]
ct4 = 0
su = []
ct = 0
el = []
for x in l:
    if str(x)[-3:] == '151':
        el.append(x)
f = sum(el)/len(el)
for x in range(len(l) - 2):
    ct7 = 0
    ct13 = 0
    #if (len(str(abs(l[x]))) == 4 and len(str(abs(l[x + 1]))) == 4 and len(str(abs(l[x + 2]))) != 4) or (len(str(abs(l[x]))) == 4 and len(str(abs(l[x+1]))) != 4 and len(str(abs(l[x+2]))) != 4) or (len(str(abs(l[x]))) != 4 and len(str(abs(l[x+1]))) == 4 and len(str(abs(l[x+2]))) == 4) or (len(str(abs(l[x]))) != 4 and len(str(abs(l[x+1]))) == 4 and len(str(abs(l[x+2]))) != 4) or (len(str(abs(l[x]))) != 4 and len(str(abs(l[x+1]))) != 4 and len(str(abs(l[x+2]))) == 4) or (len(str(abs(l[x]))) == 4 and len(str(abs(l[x+1]))) != 4 and len(str(abs(l[x+2]))) == 4):
    if l[x] % 13 == 0:
        ct13 += 1
    if l[x+1] % 13 == 0:
        ct13 += 1
    if l[x+2] % 13 == 0:
        ct13 += 1
    if l[x] % 7 == 0:
        ct7 += 1
    if l[x+1] % 7 == 0:
        ct7 += 1
    if l[x+2] % 7 == 0:
        ct7 += 1
    if ct13 > ct7:
        if l[x] > f and l[x+1] > f and l[x+2] > f:
            ct4 = 0
            if len(str(abs(l[x]))) == 4:
                ct4 += 1
            if len(str(abs(l[x + 1]))) == 4:
                ct4 += 1
            if len(str(abs(l[x + 2]))) == 4:
                ct4 += 1
            if ct4 == 1 or ct4 == 2:
                su.append(l[x]+l[x+1]+l[x+2])
                ct += 1
                print(ct13, ct7, '@@@@',  l[x], l[x + 1], l[x + 2])
print(ct,min(su))
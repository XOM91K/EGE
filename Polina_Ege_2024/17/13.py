s  = [int(x) for x in open('13.txt')]
k =0
sm  = 0
ct2 = 0
mn = 10**100
for x in s:
    if str(x)[-3:] == '151':
        k += 1
        sm += x
srar = sm/k
for x in range (len(s)-2):
    if not(len(str(abs(s[x]))) == len(str(abs(s[x + 1]))) == len(str(abs(s[x + 2]))) == 4) and (len(str(abs(s[x]))) == 4 or  len(str(abs(s[x + 1]))) == 4 or len(str(abs(s[x + 2]))) == 4):
        ct_13 = 0
        ct_7 = 0
        for y in [s[x], s[x + 1], s[x + 2]]:
            if y % 13 == 0:
                ct_13 += 1
            if y % 7 == 0:
                ct_7 += 1
        if ct_13 > ct_7:
            if s[x] > srar and s[x+1] > srar and s[x+2] > srar:
                print(s[x], s[x + 1], s[x + 2])
                ct2 +=1
                mn  = min(mn,s[x]+s[x+1]+s[x+2])
print(ct2,mn)
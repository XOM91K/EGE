l = [int(x) for x in open('20.txt')]
mx= max([x for x in l if str(x)[-2:] == '43' and len(str(abs(x))) == 5])
sm = []
for x in range(len(l) - 2):
    k = 0
    if len(str(abs(l[x]))) == 5 and str(l[x])[-2:] == '43':
        k += 1
    if len(str(abs(l[x + 1]))) == 5 and str(l[x + 1])[-2:] == '43':
        k += 1
    if len(str(abs(l[x + 2]))) == 5 and str(l[x + 2])[-2:] == '43':
        k +=1
    if k >= 1:
       if l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2 <= mx ** 2 :
            sm.append(l[x] ** 2 + l[x + 1] ** 2 + l[x + 2] ** 2)
print(len(sm), min(sm))
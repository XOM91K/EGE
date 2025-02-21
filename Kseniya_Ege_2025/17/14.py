l = [int(x) for x in open('14.txt')]
mn= min([x for x in l if x % 3 == 0])
mx= max([x for x in l if str(x)[-1] == '3'])
sm = []
for x in range(len(l) - 1):
    k = 0
    if l[x] >= mn and l[x] <= mx:
        k += 1
    if l[x + 1] >= mn and l[x + 1] <= mx:
        k += 1
    if k == 1:
        sm.append((l[x] **2) + (l[x + 1] **2))
print(len(sm), min(sm))
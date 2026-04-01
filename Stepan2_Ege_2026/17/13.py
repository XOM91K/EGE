l = [int(x) for x in open('13.txt')]
mx7 = len([d for d in l if str(abs(d))[-1] == '7'])
print(mx7)
mx=[]
for x in range(len(l) - 1):
    k = 0
    if l[x] < 0 and l[x + 1] > 0:
        k += 1
    if l[x + 1] < 0 and l[x] > 0:
        k += 1
    if k == 1:
        if l[x] + l[x + 1] < mx7:
            mx.append(l[x] + l[x + 1])
print(len(mx), max(mx))
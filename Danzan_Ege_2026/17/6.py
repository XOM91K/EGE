l = [int(x) for x in open('6.txt')]
min1 = min([x for x in l if x>0 and x%41==0])
d = []
for x in range(len(l) - 1):
    if l[x]!=l[x+1] and abs(l[x]-l[x+1])%min1 == 0:
        d.append(l[x]+l[x+1])
print(len(d), max(d))
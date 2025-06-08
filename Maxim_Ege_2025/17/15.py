l = [int(x) for x in open('15.txt')]
sr = []
a = []
for x in l:
    if x > 0:
        sr.append(x)
sr = sum(sr)/len(sr)
for x in range(len(l)-2):
    b = [l[x],l[x+1],l[x+2]]
    if (max(b)-min(b)) < sr:
        a.append(l[x]+l[x+1]+l[x+2])
print(len(a),max(a))
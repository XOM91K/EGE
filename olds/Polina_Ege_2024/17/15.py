l = [int(x) for x in open('15.txt')]
mx = 0
ct = 0
mxsum = 0
for x in l:
    if abs(x) % 100 == 68:
        mx = max(x,mx)
for x in range(len(l) - 3):
    g = [len(str(abs(l[x]))), len(str(abs(l[x + 1]))), len(str(abs(l[x + 2]))), len(str(abs(l[x + 3])))]
    if (l[x] + l[x+1] + l[x+2] + l[x+3]) >= mx:
        if g.count(2) == 1 or g.count(2) == 4:
            ct+=1
            mxsum = max(mxsum, (l[x] + l[x+1] + l[x+2] + l[x+3]))

print(ct,mxsum)
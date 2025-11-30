l = open(r"C:\Users\Zarif\Downloads\391_1 (9).txt").readline()
c = []
s = ''
for x in range(0,len(l)):
    s+= l[x]
    if "AXMM" in s:
        c.append(s[:-1])
        s = s[-3:]
print(len(max(c,key=len)))
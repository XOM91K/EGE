s=open(r'24-208 (1).txt').readline()
s=s.replace('2022', ' ')
s=s.split(' ')
mx=[]
mx2 = []
for x in range(len(s)-4):
    ln=0
    s2 = ''
    for a in range(5):
        ln+=len(s[x+a])
        s2 += s[x + a] + '2022'
    mx.append(ln)
    mx2.append(s2[:-4])
print(max(mx)+4*4)
print(len(max(mx2, key=len)))
print(max(mx2, key=len))
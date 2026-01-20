s = open(r'C:\Users\Zarif\Downloads\328_1 (6).txt').readline()
s=s.replace('CD', ' ')
s=s.split()
mx=[]
mx2=[]
for x in range(len(s)-50):
    ln=0
    s2=''
    for a in range(51):
        ln+=len(s[x+a])
        s2+=s[x+a]+'CD'
    mx.append(ln)
    mx2.append(s2[:-2])
print(max(mx)+2*50 + 2)
print(max(mx2, key=len))
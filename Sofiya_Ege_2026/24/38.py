s = open(r'C:\Users\Zarif\Downloads\1397_2 (14).txt').readline()
s=s.split('RSQ')
mx=[]
mx2=[]
for x in range(len(s)-128):
        ln=0
        #s2=''
        for a in range(129):
                ln+=len(s[x+a])
                #s2+=s[x+a]+'RSQ'
        mx.append(ln)
        #mx2.append(s2[:-130])
print(min(mx)+130*3)
#print(max(mx2, key=len))
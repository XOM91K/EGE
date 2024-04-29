s=open('1.txt').readlines()
for i in range(len(s)):
    s[i]=int(s[i])
def tr(s):
    if 999<abs(s)<10000:
        return 1
    else:
        return 0
def od(s):
    if abs(s)%100==11:
        return 1
    else:
        return 0
sred=0
h=0
for i in range(len(s)):
    if abs(s[i])%100==28:
        sred+=s[i]
        h+=1
sred=sred/h
print(sred)
k=0
mnsum=100000000000000000000000
for i in range(len(s)-2):
    if (tr(s[i])==1 or tr(s[i+1])==1 or tr(s[i+2])==1) and ((od(s[i])==1 and od(s[i+1])==1 and od(s[i+2])==0) or (od(s[i])==1 and od(s[i+1])==0 and od(s[i+2])==1) or (od(s[i])==0 and od(s[i+1])==1 and od(s[i + 2])==1)) and (s[i]>sred and s[i+1]>sred and s[i+2]>sred):
        k+=1
        mnsum=min(mnsum, (s[i]+s[i+1]+s[i+2]))
print(k, mnsum)
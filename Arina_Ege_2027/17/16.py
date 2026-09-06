l = [int(x) for x in open("16.txt")]
mx = max(l)
print(mx)
mxx=[]
for i in range(len(l)-2):
    smm = 0
    smp = 0
    if l[i]<0:
        smm+=l[i]
    else:
        smp+=l[i]
    if l[i+1]<0:
        smm+=l[i+1]
    else:
        smp+=l[i+1]
    if l[i+2]<0:
        smm+=l[i+2]
    else:
        smp+=l[i+2]
    if abs(smm)<=smp:
        if str(l[i]*l[i+1]*l[i+2])[-1] == '7':
            mxx.append(abs(l[i]*l[i+1]*l[i+2]))
print(len(mxx), max(mxx))
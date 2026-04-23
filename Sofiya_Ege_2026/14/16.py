def f15(n):
    s=[]
    while n>0:
        s.append(n%15)
        n//=15
    return s
a=3*15**1140+2*15**1025+15**923-3*15**85+2*15**74+3
b=f15(a)
ct=1
mx_ct = []
for i in range(len(b)-1):
    if b[i]==b[i+1]:
        ct+=1
        mx_ct.append(ct)
    else:
        ct=1
print(max(mx_ct))
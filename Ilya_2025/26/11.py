a = open(r'11.txt').readlines()
ct=0
sr_arf  = sum([int(i) for i in a ])/len(a)
median = int(sorted(a)[len(a)//2])
print(sr_arf, median)
for i in range(len(a)):
    if sr_arf>median:
        if int(a[i])<=sr_arf and int(a[i])>=median:
            ct+=1
    if sr_arf < median:
        if int(a[i])>=sr_arf and int(a[i])<=median:
            ct+=1
print(ct)
a = [int(i) for i in open('4.txt')]
s = 0
for i in range(len(a)):
    if a[i]%100==17:
        s= max(s,a[i])
print(s)
ct=0
maxsum=0

for i in range(len(a)-2):
    l = [a[i],a[i+1],a[i+2]]
    l2 = [a[i]%5, a[i + 1]%5, a[i + 2]%5]
    l1 = [len(str(a[i])), len(str(a[i+1])), len(str(a[i+2]))]
    if l1.count(4)==2 and sum(l)>s and l2.count(0)>=1:
        print(l, sum(l), s)
        ct+=1
        maxsum=max(maxsum,sum(l))
print(ct,maxsum)
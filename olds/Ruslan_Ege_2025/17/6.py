a = [int(x) for x in open('6.txt')]
m = []
b = []
for x in a:
    if str(abs(x))[0] == '8':
        m.append(x)
mx = max(m)
for i in range(len(a)-2):
    k = 0
    if str(abs(a[i]))[0] == '6':
        k+=1
    if str(abs(a[i+1]))[0] == '6':
        k+=1
    if str(abs(a[i+2]))[0] == '6':
        k+=1
    if k <= 1:
        if (a[i]+a[i+1]+a[i+2]) >= mx:
            b.append(a[i]+a[i+1]+a[i+2])
print(len(b), min(b))
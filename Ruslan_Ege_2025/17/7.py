a = [int(x) for x in open('7.txt')]
m = []
b = []
for x in a:
    if len(str(abs(x))) == 5 and str(abs(x))[-2:] == '25':
        m.append(x)
mx = max(m)
for i in range(len(a)-2):
    k = 0
    if len(str(abs(a[i]))) == 5 and str(abs(a[i]))[-2:] == '25':
        k+=1
    if len(str(abs(a[i+1]))) == 5 and str(abs(a[i+1]))[-2:] == '25':
        k += 1
    if len(str(abs(a[i+2]))) == 5 and str(abs(a[i+2]))[-2:] == '25':
        k+=1
    if k >= 1:
        if (a[i]**2 + a[i+1]**2 + a[i+2]**2) <= mx**2:
            b.append(a[i] ** 2+a[i+1] ** 2+a[i+2] ** 2)
print(len(b), min(b))
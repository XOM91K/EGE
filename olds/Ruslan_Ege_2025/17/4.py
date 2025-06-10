f = open('4.txt')
a = [int(x) for x in f]
b = []
p = []
for j in a:
    if str(j)[-2:] == '28':
        p.append(j)
mx = sum(p)/len(p)
for i in range(1, len(a)-2):
    n = a[i]
    m = a[i+1]
    l = a[i+2] #
    if (len(str(abs(n))) == 4) or (len(str(abs(m))) == 4) or (len(str(abs(l))) == 4):
        k = 0
        if str(n)[-2:] == '11':
            k += 1
        if str(m)[-2:] == '11':
            k += 1
        if str(l)[-2:] == '11':
            k += 1
        if k == 2:
            if n > mx and m > mx and l > mx:
                b.append(n+m+l)
print(len(b), min(b))
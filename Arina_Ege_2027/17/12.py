l = [int(x) for x in open("12.txt")]
mn = min([x for x in l if x > 0 and len(str(x)) == 4 and str(x)[-1] == '6'])
mx = []
for i in range(len(l)-2):
    k = 0
    if len(str(abs(l[i]))) == 4 and str(l[i])[-1] == '6':
        k+=1
    if len(str(abs(l[i+1]))) == 4 and str(l[i+1])[-1] == '6':
        k+=1
    if len(str(abs(l[i+2]))) == 4 and str(l[i+2])[-1] == '6':
        k+=1
    if k == 1 and l[i]+l[i+1]+l[i+2] <= mn:
        mx.append(l[i]+l[i+1]+l[i+2])
print(len(mx), max(mx))
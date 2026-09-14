l = [int(x) for x in open("500.txt")]
mx = []
mn = min([x for x in l if abs(x) % 41 == 0 and x > 0])
print(mn)
for i in range(len(l)-1):
    if l[i] != l[i+1] and abs(l[i]-l[i+1]) % mn == 0:
        mx.append(l[i]+l[i+1])
print(len(mx), max(mx))
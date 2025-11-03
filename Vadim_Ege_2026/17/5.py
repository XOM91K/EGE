f = [int(x) for x in open("5.txt")]
b = []
j = min([x for x in f if x%2==0])
for x in range(len(f) - 2):
    k = 0
    if f[x]%2==0:
        k+=1
    if f[x + 2]%2==0:
        k+=1
    if k == 1:
        if f[x + 1] % j == 0:
            b.append(f[x]+f[x + 2])
print(len(b),min(b))
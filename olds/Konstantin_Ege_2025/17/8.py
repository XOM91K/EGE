l=[int(x) for x in open('3')]
mx=0
ct=0
for x in range(len(l)-1):
    if (l[x] % 117 == min(l)) or (l[x+1] % 117 == min(l)):
        ct+=1
        mx = max(mx, l[x] + l[x+1])
print(ct)
print(mx)
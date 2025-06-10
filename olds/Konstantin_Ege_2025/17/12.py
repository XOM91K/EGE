l=[int(x) for x in open('12.txt')]
ct=0
sr = sum(l) / len(l)
r = []
for x in range(len(l)-1):
    if l[x] > sr and l[x + 1] > sr and abs((l[x] + l[x + 1])) % 100 == 31:
        ct+=1
        r.append(l[x] + l[x + 1])
print(ct)
print(max(r))
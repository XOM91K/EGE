a = int(input())
l = []
for i in range(a):
    d = int(input())
    l.append(d)
l = sorted(l)
print(l[0])
if l[-1] > 80:
    print('YES')
else:
    print('NO')
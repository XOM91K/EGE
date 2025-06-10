a = int(input())
l = []
for i in range(a):
    b = int(input())
    l.append(b)
print(max(l))
if min(l) == 0:
    print('YES')
else:
    print('NO')
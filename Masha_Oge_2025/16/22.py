n = int(input())
l = []
for x in range(n):
    a = int(input())
    l.append(a)
print(min(l))
if max(l) > 80:
    print('YES')
else:
    print('NO')
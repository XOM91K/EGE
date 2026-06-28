n = int(input())
l = []
for x in range(n):
    d = int(input())
    l.append(d)
print(max(l))
if min(l) >= 30:
    print('NO')
else:
    print('YES')
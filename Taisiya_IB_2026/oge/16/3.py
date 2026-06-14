d = int(input())
mx = []
for x in range(d):
    a = int(input())
    mx.append(a)
print(max(mx))
if min(mx) > 30:
    print('NO')
else:
    print('YES')
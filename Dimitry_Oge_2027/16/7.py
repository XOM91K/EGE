a = int(input())
neud = 0
l = []
for x in range(a):
    b = int(input())
    l.append(b)
    if b < 5:
        neud += 1
print(neud)
if max(l) == 10:
    print('YES')
else:
    print('NO')

a = int(input())
n = 0
t = False
for i in range(a):
    a = int(input())
    if a > n:
        n = a
    if a == 0:
        t = True
print(n)
if t:
    print('YES')
else:
    print('NO')

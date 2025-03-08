a = int(input())
ct = 0
vse = False
for i in range(a):
    d = int(input())
    if d < 5:
        ct += 1
    if d == 10:
        vse = True
print(ct)
if vse == True:
    print('YES')
else:
    print('NO')
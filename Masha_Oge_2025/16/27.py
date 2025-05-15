sm = 0
ct = 0
a = -1
while a != 0:
    a = int(input())
    if 1 <= a // 10 <= 9:
        sm += a
        ct += 1
if ct == 0:
    print('NO')
else:
    print(sm / ct)

a = int(input())
ct = 0
sm = 0
while a != 0:
    if a % 8 == 0:
        ct += 1
        sm += a
    a = int(input())
if ct == 0:
    print('NO')
else:
    print(sm / ct)
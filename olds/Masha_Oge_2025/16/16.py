a = -1
sm = 0
ct = 0
while a != 0:
    a = int(input())
    if a % 8 == 0 and a != 0:
        ct += 1
        sm += a
if ct > 0:
    print(sm / ct)
else:
    print('NO')
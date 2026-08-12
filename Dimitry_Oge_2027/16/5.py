a = -1
sm = 0
ct = 0
while a != 0:
    a = int(input())
    if len(str(a)) == 3 and str(a)[-1] == '5' and a % 7 == 0:
        sm += a
        ct += 1
if ct == 0:
    print('NO')
else:
    print(sm / ct)
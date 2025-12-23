d = -1
ct = 0
sm = 0
while d != 0:
    d = int(input())
    if len(str(d)) == 2:
        ct = ct + 1
        sm = sm + d
if ct == 0:
    print('NO')
else:
    print(sm / ct)
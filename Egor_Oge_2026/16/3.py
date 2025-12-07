d = -1
sm = 0
ct = 0
while d != 0:
    d = int(input())
    if d == 0:
        break
    if len(str(d)) == 3 and d % 10 == 5 and d % 7 == 0:
        ct += 1
        sm += d
if ct == 0:
    print('NO')
else:
    print(sm / ct)
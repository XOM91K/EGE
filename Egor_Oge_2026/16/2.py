 # https://examinf.ru/tasks/1163
d = -1
sr = 0
sm = 0
ct = 0
while d != 0:
    d = int(input())
    if d == 0:
        break
    if len(str(d)) == 2:
        sm = sm + d
        ct = ct + 1
if ct == 0:
    print('NO')
else:
    sr = sm / ct
    print(sr)
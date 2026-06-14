d = 1
l = []
while d != 0:
    d = int(input())
    if d == 0:
        break
    if d % 8 == 0:
        l.append(d)
if len(l) == 0:
    print('NO')
else:
    print(sum(l) / len(l))
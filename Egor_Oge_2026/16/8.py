sm = 0
ct = 0
a = int(input())
while a != 0:
    if len(str(a)) == 2:
        sm += a
        ct += 1
    a = int(input())
if ct == 0:
    print('NO')
else:
    print(sm / ct)
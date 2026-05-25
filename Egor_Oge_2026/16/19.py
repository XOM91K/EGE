d = -1
ct2 = 0
mx = -10 ** 7
while d != 0:
    d = int(input())
    sm_cif = sum(map(int, str(d)))
    ct = 0
    for x in range(1, d + 1):
        if d % x == 0:
            ct += 1
    if sm_cif > ct:
        mx = max(mx, d)
        ct2 += 1
if ct2 == 0:
    print('0 NO')
else:
    print(ct2, mx)
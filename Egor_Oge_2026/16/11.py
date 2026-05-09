a = -1
SSS = 'NO'
ct = 0
sm = 0
while a != 0:
    a = int(input())
    if (a % 7) % 2 != 0:
        ct += 1
        sm += a
if ct > 0:
    SSS = 'YES'
print(sm / ct)
if SSS == 'NO':
    print(SSS)


# 12
# 15
# 10
# 71
# 50
# 11
# 0
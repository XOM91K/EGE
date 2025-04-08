def v7(n):
    r = ''
    while n > 0:
        r += str(n%7)
        n //= 7
    return r[::-1]
N = 7**170 + 7**100
mx_x = 0
mx_z = 0
for x in range(1, 2031):
    S = N - x
    sev = v7(S)
    if sev.count('0') >= mx_z:
        mx_z = sev.count('0')
        mx_x = x
print(mx_x)
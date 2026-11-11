s = [10, 44, 196, 247, 142, 190, 2, 122, 66, 49, 204, 207, 148, 188, 95, 124, 54, 122, 213, 234, 152, 246]
BASE = 90
STEP = 31
# k_i = (BASE + i * STEP) mod 256
t = 0
el = 0
for x in s:
    if t % 2 == 0:
        el = x
        s[t] = s[t + 1]
        s[t + 1] = el
    t += 1
i = 0
for x in s:
    print(chr(x ^ ((BASE + i * STEP)) % 256), end='')
    i += 1

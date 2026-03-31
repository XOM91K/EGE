def v15(d):
    s = []
    while d > 0:
        s.append(d%15)
        d //= 15
    return s[::-1]

d = 3 * 15**1140 + 2*15**1025 + 15**923 - 3 * 15**85 + 2 * 15**74
d = v15(d)
ct = 1
mx_ct = []
for x in range(len(d) - 1):
    if d[x] == 14 and d[x + 1] == 14:
        ct += 1
    else:
        mx_ct.append(ct)
        ct = 1
print(max(mx_ct))
# 14 14 14 14
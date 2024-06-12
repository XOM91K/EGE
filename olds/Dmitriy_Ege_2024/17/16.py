s = [int(x) for x in open('16.txt')]
mx121 = 0
ct = 0
mx =0
for x in s:
    if abs(x)%1000==121:
        mx121= max(mx121,x)
print(mx121)
for x in range(len(s)-2):
    k = 0
    if len(str(abs(s[x]))) == 4 and s[x] % 2 == 0:
        k += 1
    if len(str(abs(s[x + 1]))) == 4 and s[x + 1] % 2 == 0:
        k += 1
    if len(str(abs(s[x + 2]))) == 4 and s[x + 2] % 2 == 0:
        k += 1
    if k <= 1:
        if (s[x] + s[x + 1] + s[x + 2]) <= mx121:
            ct += 1
            mx = max(mx, s[x] + s[x + 1] + s[x + 2])
print(ct, mx)
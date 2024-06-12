#5138
d = 19 ** 81 + 23 ** 709 - 4
s = ''
while d != 0:
    s += str(d % 9)
    d = d // 9
s = s[::-1]
ct = 0
print(s)
for y in range(len(s) - 1):
    for x in range(1, 8):
        if '8' + str(x) == s[y] + s[y + 1]:
            ct += 1
            break
print(ct)

s = open('21.txt').readline()
ct = 1
mx = 0
ct_gl = 0
for x in range(1, len(s)):
    if ord(s[x]) > ord(s[x - 1]):
        ct += 1
        if s[x] in 'AEIOUY':
            ct_gl += 1
    if ct_gl % 2 == 0 or ord(s[x]) <= ord(s[x - 1]):
        mx = max(mx, ct)
        ct = 1
print(mx)

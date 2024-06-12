s = open('17.txt').readline()
#AEKZIOPSW
mx = 0
ct = 1
zp = 0
gl = 0
for x in range(1, len(s)):
    d = s[x]
    if ord(s[x - 1]) < ord(s[x]):
        if s[x] in 'AEIOUY':
            gl += 1
            if gl > 1:
                ct = zp + 1
                zp = 0
                gl = 1
        else:
            zp += 1
            ct += 1
    else:
        mx = max(mx, ct)
        if s[x] in 'AEIOUY':
            gl = 1
        ct = 1
        zp = 0

print(mx)
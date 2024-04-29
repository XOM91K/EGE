s = open('13.txt').readline()
gl = False
ct = 1
mx = 0
for x in range(len(s) - 1):
    d = s[x]
    if ord(s[x]) < ord(s[x + 1]):
        ct += 1
    if (s[x] in 'AEIOUY' and gl == True) or ord(s[x]) >= ord(s[x + 1]):
        mx = max(mx, ct)
        ct = 1
        gl = False
    elif s[x] in 'AEIOUY' and gl == False:
        gl = True
print(s)
print(mx)
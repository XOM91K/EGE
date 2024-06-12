s = open('11.txt').readline()
last_len = []
print(s)
gl = False
ct = 1
mx = 0
for x in range(len(s) - 1):
    if (s[x] in 'AEIOUY' and gl == True) or ord(s[x]) >= ord(s[x + 1]):
        mx = max(mx, ct)
        ct = 1
        gl = False
    elif s[x] in 'AEIOUY' and gl == False:
        gl = True
    if ord(s[x]) < ord(s[x + 1]):
        ct += 1
print(mx)
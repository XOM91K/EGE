k = 'ABCDEFGHIJLKMNOPQRSTUVWXYZ'
print(k)
f = open('24.3')
s = f.readline()
s = s.replace('KK', '+')
for x in k:
    s = s.replace(x, '')
s = s.strip('')
s = s.split('+')


def maska(s):
    if s[:2] in '43' and s[4] == '7' and s[5] == '8' and s[9] == '3' and s[10] == '4':
        return True
    else:
        return False


mx = -1000000000
for x in range(len(s)):
    if s[x] != '' and len(s[x]) == 11 and maska(s[x]) == True:
        mx = max(mx, int(s[x]))
k = 1
mx = str(mx)
for i in range(len(mx)):
    if int(mx[i]) % 2 == 1:
        k *= int(mx[i])
print(k)

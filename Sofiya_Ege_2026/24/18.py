s=open(r'C:\Users\Zarif\Downloads\1266_1 (4).txt').readline()
s = s.split('AB')
mx_ln = []
for x in range(len(s) - 100):
    ln = 0
    for a in range(101):
        ln += len(s[x + a])
    mx_ln.append(ln)
print(max(mx_ln) + 200)
'''s=open('1').readline()
m=0
c=''
for r in range(len(s)):
    c+=s[r]
    while c.count('CD')>50:
        c=c[1:]
    m=max(m, len(c))
print(m)'''

'''s=open('1').readline()
m=0
for l in range(len(s)):
    for r in range(l+m, len(s)):
        c=s[l:r+1]
        if c.count('CD')>50:
            break
        elif c.count('CD')==50:
            m=max(m, len(c))
print(m)'''
s=open(r'C:\Users\Zarif\Downloads\1266_1 (4).txt').readline()
s = s.split('AB')
mx_ln = []
for x in range(len(s) - 100):
    ln = 0
    for a in range(101):
        ln += len(s[x + a])
    mx_ln.append(ln)
print(max(mx_ln) + 200)
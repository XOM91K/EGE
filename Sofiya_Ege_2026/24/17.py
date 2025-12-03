s=open(r'C:\Users\Zarif\Downloads\1414_1 (5).txt').readline()
s = s.split('T')
mx_ln = []
for x in range(len(s) - 100):
    ln = 0
    for a in range(0, 101):
      ln += len(s[x + a])
    mx_ln.append(ln)
print(max(mx_ln) + 100)
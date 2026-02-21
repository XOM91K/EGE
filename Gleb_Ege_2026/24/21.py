s = open(r'C:\Users\Zarif\Downloads\1414_1 (7).txt').readline()
s = s.split('T')
mx_ln = []
for x in range(len(s) - 100):
    ln = 0
    for y in range(0, 101):
        ln += len(s[x + y])
    mx_ln.append(ln + 100)
print(max(mx_ln))
import re
s = open(r'C:\Users\Zarif\Downloads\1753_1 (5).txt').readline()
m = re.findall(r'(?=([A-Z]+(?: +[A-Z]+)*\.))', s)
mx_ln = []
for x in m:
    s = x
    x = [len(d) for d in re.findall('[A-Z]+', x)]
    if x == sorted(x)[::-1]:
        mx_ln.append(len(s))
print(max(mx_ln))
import re
t=open(r'C:\Users\Zarif\Downloads\1753_1 (1).txt').readline()
m=re.findall(r'(?=([^ .]+(?:[A-Z]* )+[A-Z]+\.))', t)
mx_ln = []
for x in m:
    ln = len(x)
    x = x.replace('.', '').split()
    x2 = sorted(x, key=len)[::-1]
    if x == x2:
        mx_ln.append(ln)
print(max(mx_ln))
# print(len(max(m, key=len)))
# print((max(m, key=len)))
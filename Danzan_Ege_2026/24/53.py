import re
s = open(r'C:\Users\Zarif\Downloads\1753_1.txt').readline()
m = re.findall(r'(?=((?:[^ .]* )+[^ .]+\.))', s)
mx_ln = []
for x in m:
    ln = len(x)
    x3 = x
    x = x.replace('.', '').split()
    x2 = sorted(x, key=len)[::-1]
    if x == x2:
        mx_ln.append(ln)
        if ln == 52:
            print(x3)
print(max(mx_ln))
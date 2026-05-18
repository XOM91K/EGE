import re
s = open(r'C:\Users\Zarif\Downloads\1753_1 (3).txt').read()
m = re.findall(r'(?=([A-Z]+(?: +[A-Z]+)*\.))', s)
mx_ln = []
for x in m:
    solvers = re.findall(r'[A-Z]+', x)
    lens = [len(d) for d in solvers]
    if lens == sorted(lens)[::-1]:
        mx_ln.append(len(x))
print(max(mx_ln))

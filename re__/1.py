import re
s = ''.join(open('1.txt').readlines())
m = re.findall(r"Оборудование: (.+)?\n", s)
for x in m:
    print(x)
print(m)
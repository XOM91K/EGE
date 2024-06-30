import re
s = open('4.txt').readline()
m = re.findall('ZZ8\d{3}54\d{3}22ZZ', s)
m = max([int(d[2:-2]) for d in m])
pr = 1
for item in str(m):
    if int(item) % 2 != 0:
        pr *= int(item)
print(pr)
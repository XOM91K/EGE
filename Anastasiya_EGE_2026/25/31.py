import re
for x in range(10980,10**10,10980):
    m = re.findall(r'20[13579][13579]22[02468]*', str(x))
    if len(m) > 0 and int(m[0]) == x:
       print(x, x//10980)
# d = [9]
# print(d[0])
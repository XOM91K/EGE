import re
s = open('19.txt').readline()
m = re.findall(r'(?:[1-9]+[0-9]*[+-])*', s)
print(m)
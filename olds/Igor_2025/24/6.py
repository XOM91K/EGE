import re
s = open('6.txt').readline()
m = re.findall('(?:AD|D)(?:DAD)+(?:DA|D)', s)
print(len(max(m, key=len)))
print(m)
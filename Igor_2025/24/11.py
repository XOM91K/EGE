import re

l = open('195_1.txt'). readline()
m = re.findall('[02468][KLNF]+[02468]', l)
print(len(max(m, key=len)) - 2)
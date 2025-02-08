#https://examinf.ru/tasks/327
import re
s = open('327_1 (4).txt').readline()
m = re.findall(r'[A-Z]([1-9]\d+[02468])[A-Z]', s)
print(m)
print(max(m, key=int))
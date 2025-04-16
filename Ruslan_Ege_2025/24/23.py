import re
s = open(r'C:\Users\Zarif\Downloads\1301_1 (1).txt').readline()
m = re.findall(r'[1-9AB][0-9AB]+[02468A]', s)
print(max(m, key=len))
print(len(max(m, key=len)))
import re
s = open(r'C:\Users\Zarif\Downloads\1754_1 (3).txt').readline()
m = re.findall(r'(?=((?:[^.M]*M){112}[^.M]*\.))', s)
print(max(m, key=len))
print(len(max(m, key=len)))
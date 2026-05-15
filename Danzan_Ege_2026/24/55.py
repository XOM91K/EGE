import re
s = open(r'C:\Users\Zarif\Downloads\732_1 (2).txt').readline()
m = re.findall(r'[^XY]*X[^XY]*Y[^XY]*|[^XY]*Y[^XY]*X[^XY]*', s)
print(len(max(m, key=len)), max(m, key=len))
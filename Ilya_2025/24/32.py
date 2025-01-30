import re
s = open(r'32.txt').readline()
m = re.findall(r'(?:(?:0|[1-9]\d*)[-*])+(?:0|[1-9]\d*)', s)
print(len(max(m, key=len)))
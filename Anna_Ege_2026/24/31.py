import re
l = open(r'C:\Users\Zarif\Downloads\1600_1 (1).txt').readline()
m = re.findall(r'(?=((?:[1-9]+[*+]){49}[1-9]+))',l)
print(len(max(m, key=len)))
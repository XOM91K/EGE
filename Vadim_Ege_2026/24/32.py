import re
l = open(r'C:\Users\Zarif\Downloads\1124_1 (9).txt').readline()
m = re.findall(r'(?:(?:[1-9][0-9]*[50]|0)[*+])+(?:[1-9][0-9]*[50]|0)',l)
print(len(max(m,key=len)))
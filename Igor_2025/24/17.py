import re
s = open(r'C:\Users\Zarif\Downloads\826_1.txt').readline().replace('*', '-')
m = re.findall(r'A(?:\d+-)+\d+', s)
print(len(max(m, key=len)))
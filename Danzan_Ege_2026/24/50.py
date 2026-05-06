import re
s = open(r'C:\Users\Zarif\Downloads\1731_1 (2).txt').readline()
s = s.replace('02', '#')
m = re.findall(r'(?:[^#AEIOUY]*#){20}[^#AEIOUY]*[AEIOUY]', s)
print(len(max(m, key=len)) + 20)
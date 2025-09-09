import re
s = open(r'C:\Users\Zarif\Downloads\24_18285 (1).txt').readline()
m = re.findall('(?:[1-9]\d*[+*])+[1-9]\d*', s)
g = max(m, key=lambda d: (d.count('+') + d.count('*')))
g = g.replace('+', '*')
print(len(g.split('*')))
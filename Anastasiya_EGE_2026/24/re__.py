import re
s = 'asdXasdXasYasdaYasddYXaYYYYY'
m = re.findall(r'(?:LDR)+(?:LD|L)', s)
print(max(m, key=len))
print(m)
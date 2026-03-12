import re
s = input()
m = re.findall(r'rgb\(\d+,\d+,\d+\)', s)
print(m)
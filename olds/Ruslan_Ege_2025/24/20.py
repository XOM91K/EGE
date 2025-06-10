import re
s = open(r'C:\Users\Zarif\Downloads\1089_1.txt').readline()
m = re.findall(r'(?:[^Y.]*\.){5}[^Y.]*', s)
print(len(max(m, key=len)))
s = s.split('Y')
mx = 0
for x in s:
    d = x.split('.')
    for y in range(len(d) - 5):
      mx = max(mx, len(d[y] + d[y + 1] + d[y + 2] + d[y + 3] + d[y + 4] + d[y + 5]))
print(mx + 5)
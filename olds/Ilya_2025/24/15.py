import re
s = open('15.txt').readline().replace('CD', '#')

m = re.findall(r'(?:\w*#){160}\w*', s)
print(len(max(m, key=len)))
print(max(m, key=len).count('#'))
#\w+#
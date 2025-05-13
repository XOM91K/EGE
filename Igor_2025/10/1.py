import re
s = open('1.txt', encoding="utf-8").read()
m = re.findall(r'.[Аа]х\w+|\w+[Аа]х.|\w+[Аа]х\w+|[Аа]х-|-[Аа]х', s)
print(m)
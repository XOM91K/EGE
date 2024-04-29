import re
s = ''.join(open(r'1.txt', encoding="utf-8").readlines())
print(s)
m = re.findall(r"\b[Мм]ного\b", s)
print(m) #найти как отдельное слово
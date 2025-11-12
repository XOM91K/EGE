import re
s = open('1.txt').readline()
# m = re.findall("dg",s)
# print(m)
# print(s.count('dg'))
# m = re.findall("[0-9][0-9][0-9][0-9][0-9][0-9][0-9]",s)
# print(m)
# m = re.findall("[0-9]{3}",s)
# print(m)
# m = re.findall(r"\+7[0-9]{10}",s)
# print(m)
# m = re.findall(r"\+7\d{10}",s) # digit
# print(m)
# m = re.findall(r"\s",s) # space   \r \n \t " "
# print(m)
# m = re.findall(r"\w",s) # word [0-9A-z]
# print(m)
# Сохраняющие и несохраняющие группирующие скобки
m = re.findall(r"(?:qwe)+",s)
print(m)
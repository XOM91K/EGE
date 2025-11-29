import re
# s = open(r'C:\Users\Zarif\Downloads\195_1 (12).txt').readline()
# m = re.findall(r'2[KNLF]+2', s)
# print(max(m, key=len))
# print(len(max(m, key=len)))
s = 'НЕТНЕТНЕТТЕННТЕНЕТНЕТНЕТТНЕТТТТЕЕЕЕНЕТНЕТНЕТ'
m = re.findall(r'(?:НЕТ)+', s)
print(m)
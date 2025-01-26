import re
s = open(r'C:\Users\Zarif\Downloads\153_1 (5).txt').readline()
m = re.findall(r'(?:PNO|NPO)+', s)
print(len(max(m, key=len)) / 3)
# names = ['Тимофей', 'Ян', 'Тимур']
# print(max(names, key=len))
# print(max(names, key=str))
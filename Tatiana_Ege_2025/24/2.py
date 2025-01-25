import re
s = open(r'C:\Users\Zarif\Desktop\153_1 (4).txt').readline()
m = re.findall(r'(?:PNO|NPO)+', s)
print(len(max(m, key=len)) / 3)
# names = ['Тимофей', 'Ян', 'Артем']
# print(max(names, key=len))
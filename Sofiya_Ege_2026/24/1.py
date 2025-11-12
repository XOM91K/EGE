import re
s = open('24_demo (9).txt').readline()
m = re.findall(r'X+', s)
print(len(max(m, key=len)))
# s = ['Никита', 'Владислав', 'Ян', 'Олег']
# print(len(max(s, key=len)))
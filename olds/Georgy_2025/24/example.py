import re
s = 'asdasd)(A&D(*SD^AS(daXXsdasd;asdXXXXXaASD*(S^sdsdasdada;aXXXsdasdasd;'
m = re.findall(r'X+', s)
print(max(m, key=len))
# s = ['Никита', 'Ян', 'Святослав']
# print(max(s, key=len))
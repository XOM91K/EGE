# l = ['Абдулджаббар', 'Никита', 'Ян', 'Алексей', 'Баха']
# print(len(max(l, key=len))
# со сн
# import re
# s = ' +7444231225 +79005006077 +7900700706'
# m = re.findall(r'\+7\d{3}\d{7}', s)
# print(m)
import re
s = '123123  12389127 ,313 12893126 13 23123 132'
m = re.findall(r'\b\d{3}\b', s)
print(m) #
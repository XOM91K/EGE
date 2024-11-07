import re
s = open('/home/teacher/Загрузки/328_1.txt').readline()
m = re.findall(r'(CD\w*){50}', s)
print(m)
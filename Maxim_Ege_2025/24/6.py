import re
s = open(r'C:\Users\Zarif\Desktop\ДЕМО-2025\Доп.файлы_2025\Задание 24\demo_2025_24.txt').readline()
m = re.findall(r'(?:(?:[6-9]\d*|0)[-*])+(?:[6-9]\d*|0)', s)
print(len(max(m, key=len)))
# 1123-0*12312
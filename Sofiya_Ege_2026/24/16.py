import re
s = open(r'C:\Users\Zarif\Downloads\1062_1 (7).txt').readline()
s = s.replace('FGSW', '#')
m = re.findall(r'(?:\w*#){85}\w*', s)
print(max(m, key=len))
print(len(max(m, key=len)) + 3 * 85 + 6)
# ДОРЕШАТЬ ЗАДАЧУ
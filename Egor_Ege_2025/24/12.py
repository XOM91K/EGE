import re
s = open(r'C:\Users\Zarif\Downloads\826_1 (3).txt').readline()
m = re.findall(r'A(?:(?:[1-9]\d*|0)[-*])+(?:[1-9]\d*|0)', s)
print(len(max(m, key=len)))
print(max(m, key=len))
#6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*6*
# 1912312313132132   0
# 68884
# 0505
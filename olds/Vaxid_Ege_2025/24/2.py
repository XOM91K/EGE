import re
s = open(r'C:\Users\Zarif\Downloads\1332_1.txt').readline()
m = re.findall(r'(?:(?:[7-9]\d*|0)[-*])+(?:[7-9]\d*|0)', s)
print(len(max(m, key=len)))
# 38 * 233 - 108 - 5 * 105 * 1005 * 0 - 0 + 25
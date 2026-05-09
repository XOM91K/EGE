import re
q = []
s = open(r'C:\Users\Zarif\Downloads\1600_1 (3).txt').readline()
# print(s.find('13*619362256441365374196'))
# print(s[9573900:9573906 + 432])
m = re.findall(r'(?=((?:[1-9]\d*[+*]){49}[1-9]\d*))', s)
print(len(max(m, key=len)))
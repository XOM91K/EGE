import re
s = open(r'C:\Users\Zarif\Downloads\1698_1 (4).txt').readline()
m = re.findall(r'[^@]+(?:@gmail\.com|@yandex\.ru)', s)
print(len((max(m, key=len))))

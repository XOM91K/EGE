import re
s = open(r'C:\Users\Zarif\Downloads\1698_1.txt').readline()
m = re.findall(r'(?:[A-z0-9]*\.)+[A-z0-9]*@(?:yandex\.ru|gmail\.com)', s)
print(len(max(m, key=len)))
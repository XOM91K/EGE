import re
s = open(r'C:\Users\Zarif\Downloads\24_620_1 (2).txt').readline()
#Определите максимальное количество идущих
#подряд троек символов вида «цифра + цифра + буква»
m = re.findall(r"(?:\d\d[ABC])+", s)
print(len(max(m, key=len)) / 3)
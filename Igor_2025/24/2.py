import re
#Определите максимальное количество идущих
# подряд троек символов вида «цифра + буква + цифра»
s = open('2.txt').readline()
m = re.findall('(?:[0-9][A-z][0-9])+', s)
print(len(max(m, key=len)) // 3)
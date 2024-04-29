#import re
s = open(r'C:\Users\Zarif\Downloads\24_621_1.txt').readline()
#Определите максимальное количество
# идущих подряд троек символов
# вида «цифра + буква + цифра».


# match = re.findall(r"(?:[0-9][A-Z][0-9])+", s)
# print(len(max(match, key=len)) // 3)
s = s.replace('2', '1').replace('3', '1')
s = s.replace('B', 'A').replace('C', 'A')
s = s.replace('1A1', '#').replace('A', '1').split('1')
print(len(max(s,key=len)))
import re
s = open('2.txt').readline()
m = re.findall(r'X+', s)
print(len(max(m, key=len)))
# + - поиск от 1 символа и больше
# * - поиск от 0 символов и больше
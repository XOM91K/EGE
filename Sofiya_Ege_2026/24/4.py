import string
s = open(r'C:\Users\Zarif\Downloads\196_1 (11).txt').readline()
for x in string.ascii_uppercase:
    s = s.replace(x + x, '#')
print(s)
s = s.split('#')
print(len(max(s, key=len)))
# for x in string.ascii_uppercase:
#     s = s.replace(x + x, x + ' ' + x)
# s = s.split()
# print(len(max(s, key=len)))
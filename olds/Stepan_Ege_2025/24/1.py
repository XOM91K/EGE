import re
s = open(r'C:\Users\Zarif\Downloads\24_demo (6).txt').readline()
m = re.findall(r'X+', s)
print(m)
print(len(max(m, key=len)))
# k = 0
# while 'X' * k in s:
#     print(k)
#     k += 1
# s = ['Святослав', 'Никита', 'Яне', 'Яна']
# print(max(s, key=len))
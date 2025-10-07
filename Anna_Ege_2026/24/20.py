import string
s = open(r'C:\Users\Zarif\Downloads\174_1 (7).txt').readline()
print(s)
for x in range(26, 1, -1):
    for y in range(len(s) - x + 1):
        if len(set(s[y:y + x])) == x:
            print(x)
            exit()
# for x in string.ascii_uppercase: #AA A A
#     s = s.replace(x + x, x + ' ' + x)
# s = s.split()
# print(len(max(s, key=len)))
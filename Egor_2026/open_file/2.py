s = open('2.txt').readline()
print(s)
# for i in s:
#     print(i)
for i in range(len(s)):
    if s[i] == 'a':
        s = s[:i + 1] + 'b' + s[i + 1:]
print(s)
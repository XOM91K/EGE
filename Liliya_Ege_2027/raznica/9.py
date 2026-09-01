s = input()
print(s)
# print(s[:3])
# print(s[-3:])
for x in range(len(s) - 1):
    s = s[1:] + s[0]
    print(s)
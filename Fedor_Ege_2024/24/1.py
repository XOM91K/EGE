s = open('1.txt').readline()
for x in range(26, -1, -1):
    for z in range(len(s) - x - 1):
        if len(set(s[z: z + x])) == x:
            print(x)
            exit()
# l = ''
# mx = 0
# for x in range(len(s)):
#     if s[x] not in l:
#         l += s[x]
#     else:
#         mx = max(mx, len(l))
#         l = s[x]
# print(s)
# print(mx)

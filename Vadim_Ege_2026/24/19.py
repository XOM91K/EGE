s = open(r'C:\Users\Zarif\Downloads\1062_1 (9).txt').readline()
# s = s.split('FGSW')
mx = []
# for x in range(len(s) - 85):
#     ln = 0
#     for y in range(0, 86):
#         ln += len(s[x + y])
#     mx.append(ln)
# print(max(mx) + 85 * 4 + 6)
ln = 0
for x in range(len(s) - 1):
    for y in range(x + 1, len(s)):
        if s[x:y].count('FGSW') == 85:
            ln = max(ln, len(s[x:y]))
print(ln)
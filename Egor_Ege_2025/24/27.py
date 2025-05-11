s = open(r'C:\Users\Zarif\Downloads\24_19489.txt').readline()
r = []
ct = 2
ln = 0
mx_ln = 0
for x in range(2, len(s) - 2):
    ln = sum(r) + 3 * (len(r) - 1)
    mx_ln = max(mx_ln, ln)
    if s[x] + s[x + 1] + s[x + 2] != 'FWW':
        ct += 1
    else:
        if s[x - 2] + s[x - 1] != 'WS':
            r.append(ct)
        else:
            r = []
        ct = 0
print(mx_ln)
# s = s.replace('WSFWW', 'WSF WW')
# s = s.split('WSF ')
# mx_ln = 0
# # WWF 120
# for x in s:
#     x = x.split('WWF')
#     for y in range(len(x) - 120):
#         ln = 0
#         for z in range(0, 121):
#             ln += len(x[y + z])
#         mx_ln = max(mx_ln, ln + 120 * 3 + 4)
# print(mx_ln)

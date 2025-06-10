import re
s = open(r'C:\Users\Zarif\Downloads\390_1 (5).txt').readline()
m = re.findall(r'[^AIOYEU]?(?:[AIOYEU][^AIOYEU])+[AIOYEU]?', s)
print(len(max(m, key=len)))
# import re
# s = open(r"C:\Users\User\Downloads\390_1 (2).txt").readline()
# r = ""
# d = []
# for i in range(len(s) - 1):
#     if i == len(s) - 2:
#         if (s[i + 1] in "AEYUIO" and s[i] not in "AEYUIO") or (s[i + 1] not in "AEYUIO" and s[i] in "AEYUIO"):
#             r += s[i + 1]
#     elif s[i] in "AEYUIO" and s[i + 1] not in "AEYUIO":
#         if i != 0 and s[i - 1] not in "AEYUIO":
#             r += s[i]
#         else:
#             r += s[i]
#     elif s[i] not in "AEYUIO" and s[i + 1] in "AEYUIO":
#         if i != 0 and s[i - 1] in "AEYUIO":
#             r += s[i]
#         else:
#             r += s[i]
#     else:
#         r += s[i]
#         d.append(r)
#         r = ""
#
# print(d)
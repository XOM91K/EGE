import string
s = open(r'C:\Users\Zarif\Downloads\196_1 (10).txt').readline()
for x in string.ascii_uppercase:
    s = s.replace(x + x, f'{x} {x}')
s = s.split()
print(max(s, key=len))
print(len(max(s, key=len)))

# ct = 1
# mx = []
# print(s)
# for x in range(len(s) - 1):
#     if s[x] != s[x + 1]:
#         ct += 1
#     else:
#         mx.append(ct)
#         ct = 1
# print(max(mx))
# QQQWERTYLUR RR
#
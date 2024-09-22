c1 = int(input())
c2 = int(input())
d = (c2 - c1 + 1) // 2
if c1 % 2 == 1:
    d += 1
print(d)
# ct = 0
# for x in range(c1, c2 + 1):
#     if x % 2 == 1:
#         ct += 1
# print(ct)
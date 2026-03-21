# n = 12_500_000
# for A in range(n, 1, -1):
#     can = True
#     for x in range(1, n):
#         if ((x % 1500 == 0) <= ((x % A != 0) <= (x % 1400 != 0) or (x % 1222 != 0))) == 0:
#             can = False
#             break
#     if can:
#         print(A)
#         break
for x in range(1, 13_000_000):
    if x % 1500 == 0 and x % 1400 == 0 and x % 1222 == 0:
        print(x)
        break
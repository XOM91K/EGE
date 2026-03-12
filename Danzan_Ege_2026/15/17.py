# n = 34500
# for A in range(n, 1, -1):
#     can = True
#     for x in range(1, n):
#         if ((x % 332 == 0) <= ((x % A != 0) <= (x % 412 != 0))) == 0:
#             can = False
#             break
#     if can:
#         print(A)
#         break
for x in range(1, 136784):
    if x % 412 == 0 and x % 332 == 0:
        print(x)
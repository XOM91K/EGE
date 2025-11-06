# for A in range(0, 1000):
#     can = True
#     for x in range(0, 1000): # O(n ** 2)
#         for y in range(0, 1000): #O(n ** 3)
#             if ((x >= 27) or (2 * x < 3 * y) or (A > (x + 2) * (y - 3))) == 0:
#                 can = False
#                 break
#         if can == False:
#             break
#     if can:
#         print(A)
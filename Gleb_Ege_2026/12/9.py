# ct = 0
# for x in range(0, 770):
#     if x % 2 != 0:
#         ct += 1
# print(ct)
# #11111111111111111111111111100
# # 445
# #649
for x in range(1, 1000): # 0
    for y in range(1, 1000): # 1
        for z in range(1, 1000): # 2
            if z / x == 2:
                if x * 2 + z == 448:
                    print(y)

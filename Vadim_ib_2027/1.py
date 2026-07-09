# s = 'abracadabra'
# print(set(s))
# # def is_prime(d):
# #     for x in range(2, int(d ** 0.5) + 1):
# #         if d % x == 0:
# #             return False
# #     return True
# # # 2 147 483 647
# # print(is_prime(2_147_483_647))
def longest_common_prefix(lst):
    sl = min(lst, key=len) #flow
    i = 0
    for x in lst:
        for y in lst:
            if y[i] != sl[i]:
                return sl[:i]
        i += 1

print(longest_common_prefix(["dog", "racecar", "car"]))
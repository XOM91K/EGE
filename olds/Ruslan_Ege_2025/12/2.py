def is_prime(n):
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            return False
    return n > 1
print(is_prime(2147483647))
#
# for n in range(1, 10000):
#     s = '>' + 39*'0' + n * '1' + 39*'2'
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '22>', 1)
#         if '>2' in s:
#             s =s.replace('>2', '2>', 1)
#         if '>0' in s:
#             s =s.replace('>0', '1>', 1)
#     if is_prime(s.count('1') + s.count('2') * 2):
#         print(n)
#         break
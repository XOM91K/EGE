# # 2-ая , 8-ая и 16-ая
# d = 182
# print(bin(d)) # binary
# print(oct(d)) # octal
# print(hex(d))
# # Функция для перевода в P-ую сист. сч.
# # import string
# #
# # def vn(d, p):
# #     alf = string.digits + string.ascii_lowercase
# #     s = ''
# #     while d > 0:
# #         s = alf[d % p] + s
# #         d //= p
# #     return s
# # print(vn(182123123211232132312312312389, 15))
# # ac431663533a07267497e6979
# print(int('ac431663533a07267497e6979', 15))
# #print(int('14', 37))
# print(1 * 37 ** 1 + 4 * 37 ** 0)
# print(10 ** 500000)
s = 'ma#836213263*&w^e*&(w%xFim™®'
print(s.isdigit())
print(s.istitle())
print(s.isupper())
print(s.isascii())
# join split
s = '8, 4, 3, 2, 1'
print(s.split(','))
d = ['h', 'e', 'l', 'l', 'o']
print('$'.join(d))
# s = s.replace('О', 'А', 1)
# print(s)
# print(s.index('О'))
# print(s.rindex('О'))
# print(s.count('О'))
# print(s.zfill(10))
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())
s = 'asdasdsdasopsjasodhao'
print(len(s))
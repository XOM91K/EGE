# def xor_reverse(text, key):
#     # теперь ваш код...
#     ans = ''
#     for x in text[::-1]:
#         ans += chr(ord(x) ^ key)
#     return ans
# #в следующих задачах, нижний блок кода, пишите уже вы.
# text = input()
# key = int(input())
# print(xor_reverse(text, key))
# print(list('abc'))

# s = input() #ABCD
# k = input() #key
# ans = ''
# for y in range(len(s)):
#     ans += chr(ord(k[y % len(k)]) ^ ord(s[y]))
# print(ans)

s = input()
print(s)
print(s.encode())
# # set, list, dict, tuple
# l = [10, 3, 5, 20, -42, 59]
#
# print([x for x in l if x % 2 != 0])
#
# # SSTI {{5*9}}
# # LFI local file inclusion
# # RCE Remote Code Execution
# # path traversal
# # idor
#
#
# # XSS , CSRF ,
#
# # crypto
# # aes, rsa,
# # wireshark dump volatility
# # base64 base32 base85 xor шифра Цезаря hex byte строки
# # основы веб => sql-инъекции => БД => sqlmap
# # SSTI, LFI, RCE, PAth traveresal, IDOR , Sec. Misc, Command injection
# # crypto , forensics, СЗИ, reverse + pwn
import base64
s = 'vsosh{secret_word}'
# base64 A-Z a-z 0-9 26 + 26 + 10 = 62 + /
# print(base64.b64encode(s.encode()).decode()) # latin-1
# # base32 A-Z 01 789
# print(base64.b32encode(s.encode()).decode())
# f = base64.b85encode(s.encode()).decode()
# print(base64.b85decode(f).decode())
# s = 'hello'
# s = s.encode()
# s
# b'hello'
# list(s)
# [104, 101, 108, 108, 111]
# bytes([104, 101, 108, 108, 111])
# b'hello'
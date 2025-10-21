
# s = 'Привет'
# s = s.encode().hex()
# s2 = 'd09fd180d0b8d0b2d0b5d182'
# s2 = bytes.fromhex(s2)
# print(s2.decode())
# # s = 'Привет'
# # key = 'А'
# # answer = ''
# # # for x in range(0, 6):
# # #     answer += chr(ord(s[x]) ^ ord(key))
# # # print(answer)
# # s = 'P("%R'
# # answer = ''
# # for x in range(0, 6):
# #     answer += chr(ord(s[x]) ^ ord(key))
# # print(answer)
# vsosh{asiodhaosdihasodihqwd9812et928t1280}
import base64
s = 'VlNPU0h7UzRtXyF9'
print(base64.b64decode(s).decode())
# s = 'vsosh{asiodhaosdihasodihqwd9812et928t1280}'
# print(s)
# print(base64.b64encode(s.encode()).decode())
# s = 'dnNvc2h7YXNpb2RoYW9zZGloYXNvZGlocXdkOTgxMmV0OTI4dDEyODB9'
# print(base64.b64decode(s).decode())
s = input()
s2 = input()
answer = ''
for x in range(len(s)):
    answer += chr(ord(s[x]) ^ ord(s2))
print(answer)
import base64
# # base64 base32 base85
# s = 'vsosh{ti_nashel_flagi}'
# print(base64.b64encode(s.encode()).decode()) #base64 A-Z a-z 0-9   26 + 26 + 10 = 62  + /
# print(base64.b32encode(s.encode()).decode()) #base64 A-Z 0-9
# print(base64.b85encode(s.encode()).decode())
# # padding
s = 'R0kyREFJQlNHUTJTQU1SVEdNUURFTkJWRUFaREdPQkFHSTJUR0lCU0dNNFNBTVJSRzRRREVNWlVFQVlUUU1SQUdJMkRBSUJSSEFZU0FNUlJHNFFERU1SWkVBWkRJTkJBR0kyVEtJQlNHUTNDQU1SVUdJUURDT0JTRUFaRENOWkFHSTJERUlCU0dNNENBTUpZR01RREVNWlNFQVpERU5KQUdFM1RTSUJTR1VZUT09PT0='
s = base64.b64decode(s.encode()).decode()
s = base64.b32decode(s.encode()).decode()
s = s.split()
s = 'ðõéõîýïÙê¶ðµÙåôÿöò¶Ùòî·èá³û'
print(ord('ð') ^ ord('v'))
for x in s:
    print(chr(ord(x) ^ 134),end='')







# for x in range(0, 256):
#     ans = ''
#     for y in s:
#         ans += chr(ord(y) ^ x)
#     if 'vsosh' in ans:
#         print(ans)
# ord chr

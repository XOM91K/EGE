# def xor_with_string_key(text: str, keys: list):
#     text = text.encode('latin1')
#     decoded_str = ''
#     for x in range(len(text)):
#         decoded_str += chr(text[x] ^ keys[x % len(keys)])
#     return decoded_str
# text = input()
# keys = list(map(int, input().split()))
# print(xor_with_string_key(text, keys))
text = 'Text'
keys = [1, 2, 7]
text2 = text.encode()
print(chr(text2[0] ^ 1 ^ 2 ^ 7), text2[1] ^ 2)
print(chr(ord(text[0]) ^ 1), ord(text[1]) ^ 2)
import base64
st = 'flag{Base64_XOR_Flag}'
key = 0x42
flag = [bytes((ord(x) ^ 0x42)) for x in st]

print(flag)
flag = [base64.b64encode(x) for x in flag]
print("Flag:", flag)
# encoded_flag = "-37 -47 -36 -38 -58 -27 -14 -17 -30 -13 -14 -23 -30 -5 -47 -36 -38 -64"
# encoded_flag = encoded_flag.split(' ')
# enc = [int(x) for x in encoded_flag]
# key = 0x42
# flag = "".join(chr(~(byte ^ key)) for byte in enc)
# print("Flag:", flag)
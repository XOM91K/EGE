with open("flag.txt", "r") as file:
    real_flag = file.read()[:-1]

key = "my_key_is_same_length_its_my_fault_yep"
something_temporary_or_not = bytes(ord(a) ^ ord(b) for a,b in zip(real_flag[0], key[0]))
so_encoded = b"" + something_temporary_or_not + bytes(real_flag[1:].encode())

for i in range(1, len(so_encoded)):
    qwerty_param = bytes(a ^ ord(b) for a,b in zip(so_encoded[:i], key[:i]))
    so_encoded = qwerty_param + bytes(real_flag[i+1:].encode())

with open("encoded2.txt", "wb") as file:
    file.write(so_encoded)

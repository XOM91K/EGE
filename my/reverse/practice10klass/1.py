flag = "ctfinf{x0r_x0r_n0t_3asy}"
encrypted = []

for c in flag:
    val = ord(c)
    val ^= 0x2F      # XOR с 0x2F
    val ^= 0xA1      # XOR с 0xA1
    val = ~val & 0xFF  # NOT (инверсия) + маска на 1 байт
    encrypted.append(val)

print("Encrypted bytes:", encrypted)
print("Hex:", [hex(x) for x in encrypted])
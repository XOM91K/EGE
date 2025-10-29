import ipaddress
ct2 = 0
for A in range(1, 256):
    can = True
    for x in ipaddress.ip_network(f'246.81.65.{A}/255.255.255.224', 0):
        x = bin(int(x))[2:].zfill(32)
        if x[-16:-8].count('0') <= x[-8:].count('0'):
            can = False
            break
    if can:
        ct2 += 1
print(ct2)
            # 11111111000000001111111100000000
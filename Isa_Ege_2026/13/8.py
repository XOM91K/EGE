import ipaddress
ct_A = []

for A in range(0, 256):
    can = True
    for x in ipaddress.ip_network(f'246.81.65.{A}/255.255.255.224', 0).hosts():
        x = bin(int(x))[2:].zfill(32)
        if x[-16:-8].count('0') <= x[-8:].count('0'):
            can = False
    if can:
        ct_A.append(A)
print(len(set(ct_A)))
import ipaddress
#342
ct =0
for A in range(0, 256):
    can = True
    for x in ipaddress.ip_network(f'246.81.65.{A}/255.255.255.224', False):
        x = bin(int(x))[2:].zfill(32)
        b3 = x[16:24]
        b4 = x[24:]
        if b3.count('0') <= b4.count('0'):
            can = False
            break
    if can:
        ct += 1
print(ct)
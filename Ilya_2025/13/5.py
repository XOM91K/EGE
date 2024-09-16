import ipaddress
ct = 0
for A in range(0, 256):
    can = True
    network = ipaddress.IPv4Network(f'246.81.65.{A}/255.255.255.224', False).network_address
    for x in ipaddress.ip_network(f'{network}/255.255.255.224', False):
        x = bin(int(x))[2:].zfill(32)
        tr = x[16:24]
        ch = x[24:]
        #print(tr, ch)
        if tr.count('0') <= ch.count('0'):
            can = False
    if can:
        ct += 1
print(ct)
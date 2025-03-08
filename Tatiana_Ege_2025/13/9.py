import ipaddress
for mask in range(15, 33):
    ipnet1 = ipaddress.ip_network(f'211.188.211.49/{mask}', 0)
    ipnet2 = ipaddress.ip_network(f'211.188.200.115/{mask}', 0)
    if ipnet1 == ipnet2:
        ct = 0
        for y in ipnet1:
            y = bin(int(y))[2:].zfill(32)
            if y.count('1') % 2 != 0:
                ct += 1
        print(ct)
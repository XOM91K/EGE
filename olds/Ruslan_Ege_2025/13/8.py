import ipaddress
for mask in range(15, 33):
    net1 = ipaddress.ip_network(f'126.115.78.15/{mask}', 0)
    net2 = ipaddress.ip_network(f'126.115.84.26/{mask}', 0)
    if net1 == net2:
        ct = 0
        for x in net1:
            x = bin(int(x))[2:].zfill(32)
            if x.count('1') == 22:
                ct += 1
        print(ct)
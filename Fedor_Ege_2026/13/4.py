import ipaddress
for mask in range(15, 33):
    net1 = ipaddress.ip_network(f'211.188.211.49/{mask}', 0)
    net2 = ipaddress.ip_network(f'211.188.200.115/{mask}', 0)
    if net1 == net2:
        ct = 0
        for x in net1:
            x = bin(int(x))[2:].zfill(32)
            if x.count('1') % 2 != 0:
                ct += 1
        print(ct)
        print(2 ** (32 - mask) / 2)
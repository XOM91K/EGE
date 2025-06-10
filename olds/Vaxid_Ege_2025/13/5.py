import ipaddress
for mask in range(16, 33):
    ip_net1 = ipaddress.ip_network(f'211.188.211.49/{mask}', 0)
    ip_net2 = ipaddress.ip_network(f'211.188.200.115/{mask}', 0)
    if ip_net1 == ip_net2:
        k = 0
        for x in ip_net1:
            x = bin(int(x))[2:].zfill(32)
            if x.count('1') % 2 != 0:
                k += 1
        print(k)
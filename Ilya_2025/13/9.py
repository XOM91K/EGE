import ipaddress
mn_ct = 10 ** 10
for mask in range(10, 33):
    net1 = ipaddress.ip_network(f'211.188.211.49/{mask}', 0)
    net2 = ipaddress.ip_network(f'211.188.200.115/{mask}', 0)
    if net1 == net2:
        ct = 0
        for ip in net1:
            ip = bin(int(ip))[2:].zfill(32)
            if ip.count('1') % 2 != 0:
                ct += 1
        mn_ct = min(mn_ct, ct)
print(mn_ct)
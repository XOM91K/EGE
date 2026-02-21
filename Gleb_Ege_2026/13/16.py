import ipaddress
for mask in range(15, 33):
    net = ipaddress.ip_network(f'121.96.174.205/{mask}', 0)
    ct = 0
    for ip in net:
        ip = bin(int(ip))[2:].zfill(32)
        if ip.count('1') == 12:
            ct += 1
    if ct == 10:
        print(mask, bin(int(net.netmask))[2:].zfill(32).count('1'))
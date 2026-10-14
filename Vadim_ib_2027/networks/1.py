import ipaddress
ips = ['192.168.10.5', '192.168.10.32', '192.168.10.16', '192.168.10.9']
for mask in range(15, 33):
    net = ipaddress.ip_network(f'192.168.10.5/{mask}', 0)
    ct = 0
    net = [str(x) for x in net]
    #print(list(net))
    for ip in ips:
        if ip in net:
            ct += 1
    if ct == 4:
        print(mask)
    else:
        print(ct, mask)
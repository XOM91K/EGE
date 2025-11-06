import ipaddress
for mask in range(15, 33):
    net = ipaddress.ip_network(f'121.96.174.205/{mask}', 0)
    ct = 0
    for x in net:
        x = bin(int(x))[2:].zfill(32)
        if x.count('1') == 12:
            ct += 1
    if ct == 10:
        print(net)
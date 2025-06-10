import ipaddress
for mask in range(15, 33):
    net = ipaddress.ip_network(f'143.131.211.37/{mask}', 0)
    ct = 0
    for y in net:
        y = bin(int(y)).zfill(32)
        if y.count('1') == 10:
            ct += 1
    if ct == 15:
        print(net, mask)
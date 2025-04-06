import ipaddress
for mask in range(0, 33):
    net = ipaddress.ip_network(f'14.253.0.0/{mask}', 0)
    ip = ipaddress.ip_address('14.253.13.6')
    if ip in net:
        ip = bin(int(ip))[2:].zfill(32)
        print(net.netmask, ip)
for x in ipaddress.ip_network('14.253.0.0/255.128.0.0', 0):
    x = bin(int(x))[2:].zfill(32)
    if x.count('1') > 25:
        print(x.count('1'))

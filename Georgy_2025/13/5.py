import ipaddress
for mask in range(15, 33):
    ip = ipaddress.ip_network(f'92.52.42.0/{mask}', 0)
    ip2 = ipaddress.ip_address('92.52.42.52')
    if ip2 in ip:
        print(mask, ip.netmask)

#23 - 32